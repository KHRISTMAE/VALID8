from unittest.mock import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Database.database import Base
from fastapi import FastAPI
from sqlalchemy import create_engine


class Attendance(Base):
    __tablename__ = 'attendance'

    attendanceID = Column(Integer, primary_key=True, autoincrement=True)
    studentID = Column(Integer, ForeignKey('student.studentID'), nullable=False)
    eventID = Column(Integer, ForeignKey('event.eventID'), nullable=False)
    checkInTime = Column(DateTime, nullable=True)
    midEventCheckpoint = Column(DateTime, nullable=True)
    checkOutTime = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)

    student = relationship("Student", back_populates="attendances")
    event = relationship("Event", back_populates="attendances")

    def __init__(self, student, event, checkInTime=None, status=''):
        self.student = student
        self.event = event
        self.checkInTime = checkInTime
        self.status = status
