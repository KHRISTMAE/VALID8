from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    eventName: str
    dateAndTime: datetime
    location: str
    organizerID: int

class EventResponse(BaseModel):
    eventID: int
    eventName: str
    dateAndTime: datetime
    location: str
    organizerID: int

    class Config:
        from_attributes = True
