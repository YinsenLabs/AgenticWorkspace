import pytest
from agentic_workspace.tools.google_calendar.actions import GoogleCalendar


# pytest insert event
def test_google_calendar_actions():
    with GoogleCalendar() as calendar:
        response = calendar.insert_event({
            'summary': 'Test Event',
            'description': 'This is a test event',
            'start': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            },
            'end': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            }
        })

        assert response is not None
        assert response['summary'] == 'Test Event'
        assert response['description'] == 'This is a test event'
        assert response['start']['dateTime'] == '2023-05-01T23:00:00+07:00'
        assert response['end']['dateTime'] == '2023-05-01T23:00:00+07:00'

        # delete the event
        calendar.delete_event(response['id'])

# pytest list event
def test_google_calendar_list_event():
    with GoogleCalendar() as calendar:
        response = calendar.list_event(timeMin='2023-05-01T23:00:00+07:00', maxResults=10)
        assert response is not None
        assert len(response) > 0

# pytest get event
def test_google_calendar_get_event():
    with GoogleCalendar() as calendar:
        # insert an event
        inserted_event = calendar.insert_event({
            'summary': 'Test Event',
            'description': 'This is a test event',
            'start': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            },
            'end': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            }
        })

        # get the event
        response = calendar.get_event(inserted_event['id'])
        assert response is not None
        assert response['summary'] == 'Test Event'
        assert response['start']['dateTime'] == '2023-05-01T23:00:00+07:00'
        assert response['end']['dateTime'] == '2023-05-01T23:00:00+07:00'

        # delete the event
        calendar.delete_event(inserted_event['id'])

# pytest update event
def test_google_calendar_update_event():
    with GoogleCalendar() as calendar:
        # insert an event
        inserted_event = calendar.insert_event({
            'summary': 'Test Event',
            'description': 'This is a test event',
            'start': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            },  
            'end': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            }
        })  

        # update the event
        response = calendar.update_event(inserted_event['id'], {
            'summary': 'Updated Event'
        })
        assert response is not None
        assert response['summary'] == 'Updated Event'

        # delete the event
        calendar.delete_event(inserted_event['id'])

# pytest delete event
def test_google_calendar_delete_event():
    with GoogleCalendar() as calendar:
        # insert an event
        inserted_event = calendar.insert_event({
            'summary': 'Test Event',
            'description': 'This is a test event',
            'start': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            },
            'end': {
                'dateTime': '2023-05-01T23:00:00+07:00',
                'timeZone': 'America/New_York'
            }
        })

        # delete the event
        deleted = calendar.delete_event(inserted_event['id'])
        assert deleted is True
