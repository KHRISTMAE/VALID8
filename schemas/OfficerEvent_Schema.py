from pydantic import BaseModel
from typing import Optional

# Base schema for common fields
class OfficerEventBase(BaseModel):
    officerID: int
    eventID: int

# Create schema: For creating a new OfficerEvent
class OfficerEventCreate(OfficerEventBase):
    pass

# Update schema: For updating an existing OfficerEvent
class OfficerEventUpdate(OfficerEventBase):
    pass

# Response schema: For returning OfficerEvent data
class OfficerEventResponse(OfficerEventBase):
    officerID: int
    eventID: int

    class Config:
        from_attributes = True  # This allows SQLAlchemy ORM models to be used
