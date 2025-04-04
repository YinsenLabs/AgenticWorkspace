from pydantic import BaseModel, Field
from agentic_workspace.models.base import BaseOutputModel


class Time(BaseModel):
    dateTime: str = Field(description="Time value as a RFC3339 timestamp")
    timeZone: str = Field(description="Time zone value e.g: Asia/Ho_Chi_Minh")

class CalendarEventModel(BaseOutputModel):
    """ Response class for calendar api """
    
    summary: str = Field(..., title="Summary", description="The generated summary to use as a title of calendar")
    description: str = Field(description='A short description of event as list to track')
    start: Time = Field(description='Time start')
    end: Time = Field(description='Time end')
