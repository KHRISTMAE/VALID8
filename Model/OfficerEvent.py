from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base

class OfficerEvent(Base):
    __tablename__ = 'officer_event'

    officerID = Column(Integer, ForeignKey('ssg_officer.officerID'), primary_key=True)
    eventID = Column(Integer, ForeignKey('event.eventID'), primary_key=True)

    officer = relationship("SSGOfficer", back_populates="events")
    event = relationship("Event", back_populates="officers")

    def __init__(self, officer, event):
        self.officer = officer
        self.event = event
        self.officerID = officer.officerID
        self.eventID = event.eventID
