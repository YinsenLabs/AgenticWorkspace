import os
from google import genai
from agentic_workspace.models.calendar_event import CalendarEventModel


def call_gemini_calendar_event(prompt:str):
    """Call Gemini API to create google api event denifition and parse output"""
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[CalendarEventModel],
        },
    )

    return response.parsed # List[CalendarEventModel]
