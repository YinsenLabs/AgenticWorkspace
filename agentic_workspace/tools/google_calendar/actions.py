from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import Optional, List
from datetime import datetime, timedelta, timezone

from agentic_workspace.tools.google_calendar.auth import get_calendar_credentials


# Google Calendar API
class GoogleCalendar:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GoogleCalendar, cls).__new__(cls)
        return cls._instance

    def __init__(self, calendar_id: str = 'primary'):
        if not self._initialized:
            # Get credentials
            creds = get_calendar_credentials()

            # Build the Google Calendar API service 
            self.service = build('calendar', 'v3', credentials=creds)
            self.calendar_id = calendar_id
            self._initialized = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.service:
            self.service.close()

    # Insert event
    def insert_event(self, event: dict) -> Optional[dict]:
        try:
            event = self.service.events().insert(calendarId=self.calendar_id, body=event).execute()
            return event
        except HttpError as e:
            print(f"Error inserting event: {e}")
            return None

    # List event
    def list_event(self, timeMin: Optional[str] = None, maxResults: int = 10) -> List[dict]:
        try:
            # Call the Calendar API
            events_result = self.service.events().list(
                calendarId=self.calendar_id,
                timeMin=timeMin,
                maxResults=maxResults,
                singleEvents=True,
                orderBy='startTime',
            ).execute()

            events = events_result.get('items', [])
            return events
        except HttpError as e:
            print(f"Error listing events: {e}")
            return []
    
    # Get event
    def get_event(self, event_id: str) -> Optional[dict]:
        try:
            event = self.service.events().get(calendarId=self.calendar_id, eventId=event_id).execute()
            return event
        except HttpError as e:
            print(f"Error getting event: {e}")
            return None

    # Update event
    def update_event(self, event_id: str, event: dict) -> Optional[dict]:
        try:
            body = self.get_event(event_id)

            # Update the event
            for key, value in event.items():
                body[key] = value

            event = self.service.events().update(calendarId=self.calendar_id, eventId=event_id, body=body).execute()
            return event
        except HttpError as e:
            print(f"Error updating event: {e}")
            return None

    # Delete event
    def delete_event(self, event_id: str) -> bool:
        try:
            if self.get_event(event_id)['status'] == 'cancelled':
                return False
            
            self.service.events().delete(calendarId=self.calendar_id, eventId=event_id).execute()
            return True
        except HttpError as e:
            print(f"Error deleting event: {e}")
            return False

    def query_free_busy(self, timeMin: Optional[str] = None, timeMax: Optional[str] = None, items: Optional[List[str]] = None) -> List[dict]:
        try:
            # Default values if not provided
            if not timeMin:
                timeMin = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            if not timeMax:
                timeMax = (datetime.now(timezone.utc) + timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
            if not items:
                items = [{"id": "primary"}]

            body = {
                "timeMin": timeMin,
                "timeMax": timeMax,
                "items": items
            }

            free_busy = self.service.freebusy().query(body=body).execute()
            return free_busy
        
        except HttpError as e:
            print(f"Error querying free busy: {e}")
            return []
