# schemas.py
from pydantic import BaseModel
from datetime import datetime

class AttendanceCreate(BaseModel):
    studentID: int
    eventID: int
    checkInTime: datetime = None
    status: str = ''

class AttendanceUpdate(BaseModel):
    studentID: int
    eventID: int
    checkInTime: datetime = None
    status: str = ''

class AttendanceOut(BaseModel):
    attendanceID: int
    studentID: int
    eventID: int
    checkInTime: datetime
    midEventCheckpoint: datetime = None
    checkOutTime: datetime = None
    status: str

    class Config:
        from_attributes = True
