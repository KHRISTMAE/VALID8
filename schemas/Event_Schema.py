from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    eventName: str
    dateAndTime: datetime
    location: str
    organizerID: int

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    eventName: Optional[str] = None
    dateAndTime: Optional[datetime] = None
    location: Optional[str] = None
    organizerID: Optional[int] = None

class EventResponse(EventBase):
    eventID: int

    class Config:
        from_attributes = True  # This is necessary for reading data from the ORM models
