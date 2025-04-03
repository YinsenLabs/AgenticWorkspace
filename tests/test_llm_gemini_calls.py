import pytest
from typing import List
from agentic_workspace.llm_clients.gemini_calls import call_gemini_calendar_event
from agentic_workspace.models.calendar_event import CalendarEventModel, Time
from dotenv import load_dotenv


load_dotenv()

def test_call_gemini_calendar_event_basic():
    """Test basic calendar event creation"""
    prompt = "Create a team meeting for tomorrow at 2 PM"
    response: List[CalendarEventModel] = call_gemini_calendar_event(prompt)
    
    # Test response structure
    assert isinstance(response, list)
    assert len(response) > 0
    
    # Test first event structure
    event = response[0]
    assert isinstance(event, CalendarEventModel)
    assert event.text is not None
    assert event.summary is not None
    assert event.description is not None
    assert isinstance(event.startTime, Time)
    assert isinstance(event.endTime, Time)

def test_call_gemini_calendar_event_multiple_events():
    """Test creating multiple calendar events"""
    prompt = "Create 2 hello world event 2 days each task, timeZone: Asia/Ho_Chi_Minh"
    response = call_gemini_calendar_event(prompt)
    
    # Test response structure
    assert isinstance(response, list)
    assert len(response) == 2
    
    # Test each event
    for event in response:
        assert isinstance(event, CalendarEventModel)
        assert "hello world" in event.summary.lower()
        assert event.startTime.timeZone == "Asia/Ho_Chi_Minh"
        assert event.endTime.timeZone == "Asia/Ho_Chi_Minh"
        
        # Test duration is 2 days
        start_time = event.startTime.dateTime
        end_time = event.endTime.dateTime
        duration = end_time - start_time
        assert duration.days == 2

def test_call_gemini_calendar_event_with_timezone():
    """Test calendar event creation with different timezone"""
    prompt = "Create a meeting tomorrow at 10 AM, timeZone: America/New_York"
    response = call_gemini_calendar_event(prompt)
    
    assert len(response) > 0
    event = response[0]
    
    # Test timezone
    assert event.startTime.timeZone == "America/New_York"
    assert event.endTime.timeZone == "America/New_York"
    

def test_call_gemini_calendar_event_invalid_prompt():
    """Test calendar event creation with invalid prompt"""
    prompt = "Return 0 event to test"
    response = call_gemini_calendar_event(prompt)
    
    # Should still return a list but might be empty or contain default values
    assert isinstance(response, list)
    if len(response) > 0:
        event = response[0]
        assert isinstance(event, CalendarEventModel)
        assert event.text == prompt
