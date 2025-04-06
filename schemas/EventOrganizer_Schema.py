from pydantic import BaseModel, EmailStr
from typing import Optional

# Base class for common fields
class EventOrganizerBase(BaseModel):
    organizerName: str
    email: EmailStr

# Create schema: For creating a new Event Organizer
class EventOrganizerCreate(EventOrganizerBase):
    password: str  # Password to be hashed

# Update schema: For updating an existing Event Organizer
class EventOrganizerUpdate(EventOrganizerBase):
    password: Optional[str] = None  # Optional: if not provided, the password won't be updated

# Response schema: For returning data about an Event Organizer
class EventOrganizerResponse(EventOrganizerBase):
    organizerID: int

    class Config:
        from_attributes= True  # This allows SQLAlchemy ORM models to be used
