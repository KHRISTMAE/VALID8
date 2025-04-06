from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal
from .Student import Student

# Using string reference to avoid circular imports
class Attendance(Base):
    __tablename__ = 'attendance'

    attendanceID = Column(Integer, primary_key=True, autoincrement=True)
    studentID = Column(Integer, ForeignKey('student.studentID'), nullable=False)
    eventID = Column(Integer, ForeignKey('event.eventID'), nullable=False)
    checkInTime = Column(DateTime, nullable=True)
    midEventCheckpoint = Column(DateTime, nullable=True)
    checkOutTime = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)

    student = relationship('Student', back_populates='attendance')
    event = relationship('Event', back_populates='attendance')


    def __init__(self, studentID, eventID, checkInTime=None, status=''):
        self.studentID = studentID
        self.eventID = eventID
        self.checkInTime = checkInTime
        self.status = status

    @property
    def formatted_id(self):
        """Returns formatted attendance ID if assigned; otherwise, 'Pending ID'."""
        return f"A{self.attendanceID}" if self.attendanceID is not None else "Pending ID"


# ✅ Encapsulating session logic in a function
def fetch_first_attendance():
    """Fetches the first attendance record and prints its formatted ID."""
    with SessionLocal() as db:
        attendance = db.query(Attendance).first()
        if attendance:
            print(attendance.formatted_id)  # Expected: 'A1', 'A2', etc.
        else:
            print("No attendance records found.")
