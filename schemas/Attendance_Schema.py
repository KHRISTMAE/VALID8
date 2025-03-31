from pydantic import BaseModel
from datetime import datetime

class AttendanceBase(BaseModel):
    user_id: int
    event_id: int

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # allows SQLAlchemy models as responses
