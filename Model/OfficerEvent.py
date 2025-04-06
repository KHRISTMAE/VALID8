from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base


class OfficerEvent(Base):
    __tablename__ = 'officer_event'

    officerID = Column(Integer, ForeignKey('ssg_officer.officerID'), primary_key=True)
    eventID = Column(Integer, ForeignKey('event.eventID'), primary_key=True)

    # Define the relationships for many-to-many
    officer = relationship('SSGOfficer', back_populates='officer_event')
    event = relationship('Event', back_populates='officer_event')

    def __init__(self, officer, event):
        self.officer = officer
        self.event = event

    