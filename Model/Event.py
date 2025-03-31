from sqlalchemy import Column, Integer, String, DateTime, ForeignKey 
from sqlalchemy.orm import relationship, declarative_base 
from Database.database import Base

class Event(Base):
    __tablename__ = 'event'

    eventID = Column(Integer, primary_key=True, autoincrement=True)
    eventName = Column(String, nullable=False)
    dateAndTime = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    organizerID = Column(Integer, ForeignKey('event_organizer.organizerID'), nullable=False)

    organizer = relationship("EventOrganizer", back_populates="events")
    attendances = relationship("Attendance", back_populates="event", cascade="all, delete-orphan")

    def __init__(self, eventName, dateAndTime, location, organizer):
        self.eventName = eventName
        self.dateAndTime = dateAndTime
        self.location = location
        self.organizer = organizer

    def __repr__(self):
        return f"<Event(eventID={self.eventID}, eventName='{self.eventName}', dateAndTime={self.dateAndTime}, location='{self.location}')>"
