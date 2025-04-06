import pytest
from agentic_workspace.llm_clients.promt_template import calendar_event_prompt


# test prompt template for calendar event creation from text input
def test_design_calendar_event_prompt():
    prompt = calendar_event_prompt(
        objective="Test prompt",
    )

    assert len(prompt) > 0
    assert isinstance(prompt, str)
    assert "Test prompt" in prompt
    assert "calendar event creator" in prompt
    assert "Create a calendar event from the given text" in prompt
    assert "The event should be created in the next 30 days" in prompt
    assert "The user is a busy person who needs to create a calendar event" in prompt
    assert "Re-emphasize the key aspects of the prompt, especially the instructions, constraints, etc." in prompt
    