import pytest
from datetime import datetime
from agentic_workspace.models.calendar_event import CalendarEventModel, Time

def test_time_model_structure():
    """Test the structure of Time model"""
    # Test valid time data
    valid_time = Time(
        dateTime="2024-06-11T07:00:00+07:00",
        timeZone="UTC"
    )
    
    assert valid_time.dateTime == "2024-06-11T07:00:00+07:00"
    assert valid_time.timeZone == "UTC"
    assert isinstance(valid_time.dateTime, str)
    assert isinstance(valid_time.timeZone, str)

def test_calendar_event_model_structure():
    """Test the structure and validation of CalendarEventModel"""
    # Test valid data
    valid_event = CalendarEventModel(
        text="Create a team meeting for tomorrow at 2 PM",
        summary="Team Meeting",
        description="Weekly team sync",
        start=Time(
            dateTime="2024-06-11T07:00:00+07:00",
            timeZone="UTC"
        ),
        end=Time(
            dateTime="2024-06-11T07:00:00+07:00",
            timeZone="UTC"
        )
    )
    
    # Test required fields
    assert valid_event.summary == "Team Meeting"
    assert valid_event.description == "Weekly team sync"
    assert isinstance(valid_event.start, Time)
    assert isinstance(valid_event.end, Time)
    
    # Test time values
    assert valid_event.start.dateTime == "2024-06-11T07:00:00+07:00"
    assert valid_event.end.dateTime == "2024-06-11T07:00:00+07:00"
    assert valid_event.start.timeZone == "UTC"
    assert valid_event.end.timeZone == "UTC"

def test_calendar_event_model_serialization():
    """Test serialization of CalendarEventModel"""
    event = CalendarEventModel(
        text="Create a team meeting for tomorrow at 2 PM",
        summary="Team Meeting",
        description="Weekly team sync",
        start=Time(
            dateTime="2024-06-11T07:00:00+07:00",
            timeZone="UTC"
        ),
        end=Time(
            dateTime="2024-06-11T07:00:00+07:00",
            timeZone="UTC"
        )
    )
    
    # Test model_dump
    event_dict = event.model_dump()
    assert event_dict["summary"] == "Team Meeting"
    assert event_dict["description"] == "Weekly team sync"
    assert event_dict["start"]["dateTime"] == "2024-06-11T07:00:00+07:00"
    assert event_dict["end"]["dateTime"] == "2024-06-11T07:00:00+07:00"
