import pytest
from datetime import datetime
from agentic_workspace.models.calendar_event import CalendarEventModel, Time

def test_time_model_structure():
    """Test the structure of Time model"""
    # Test valid time data
    valid_time = Time(
        dateTime=datetime(2024, 4, 1, 10, 0, 0),
        timeZone="UTC"
    )
    
    assert valid_time.dateTime == datetime(2024, 4, 1, 10, 0, 0)
    assert valid_time.timeZone == "UTC"
    assert isinstance(valid_time.dateTime, datetime)
    

def test_calendar_event_model_structure():
    """Test the structure and validation of CalendarEventModel"""
    # Test valid data
    valid_event = CalendarEventModel(
        text="Create a team meeting for tomorrow at 2 PM",
        summary="Team Meeting",
        description="Weekly team sync",
        startTime=Time(
            dateTime=datetime(2024, 4, 1, 10, 0, 0),
            timeZone="UTC"
        ),
        endTime=Time(
            dateTime=datetime(2024, 4, 1, 10, 0, 0),
            timeZone="UTC"
        )
    )
    
    # Test required fields
    assert valid_event.summary == "Team Meeting"
    assert valid_event.description == "Weekly team sync"
    assert isinstance(valid_event.startTime, Time)
    assert isinstance(valid_event.endTime, Time)
    
    # Test time values
    assert valid_event.startTime.dateTime == datetime(2024, 4, 1, 10, 0, 0)
    assert valid_event.endTime.dateTime == datetime(2024, 4, 1, 10, 0, 0)
    assert valid_event.startTime.timeZone == "UTC"
    assert valid_event.endTime.timeZone == "UTC"

def test_calendar_event_model_serialization():
    """Test serialization of CalendarEventModel"""
    event = CalendarEventModel(
        text="Create a team meeting for tomorrow at 2 PM",
        summary="Team Meeting",
        description="Weekly team sync",
        startTime=Time(
            dateTime=datetime(2024, 4, 1, 10, 0, 0),
            timeZone="UTC"
        ),
        endTime=Time(
            dateTime=datetime(2024, 4, 1, 10, 0, 0),
            timeZone="UTC"
        )
    )
    
    # Test model_dump
    event_dict = event.model_dump()
    assert event_dict["summary"] == "Team Meeting"
    assert event_dict["description"] == "Weekly team sync"
    assert event_dict["startTime"]["dateTime"].isoformat() == "2024-04-01T10:00:00"
    assert event_dict["endTime"]["dateTime"].isoformat() == "2024-04-01T10:00:00"
