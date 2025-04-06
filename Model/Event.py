from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal
class Event(Base):
    __tablename__ = 'event'
    
    eventID = Column(Integer, primary_key=True, autoincrement=True)
    eventName = Column(String, nullable=False)
    dateAndTime = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    organizerID = Column(Integer, ForeignKey('event_organizer.organizerID', ondelete="CASCADE"), nullable=False)
    
    # Use string-based references for all relationships to avoid circular imports
    event_organizer = relationship('EventOrganizer', back_populates = 'event_list')
    attendance = relationship('Attendance', back_populates='event')
    officer_event = relationship('OfficerEvent', back_populates='event')
    
    def __init__(self, eventName, dateAndTime, location, organizerID):
        self.eventName = eventName
        self.dateAndTime = dateAndTime
        self.location = location
        self.organizerID = organizerID  # Store only ID
    
    def __repr__(self):
        return (f"<Event(eventID={self.eventID}, eventName='{self.eventName}', "
                f"dateAndTime={self.dateAndTime}, location='{self.location}', "
                f"organizer='{self.event_organizer.organizerName if self.event_organizer else 'Unknown'}')>")
    
    @property
    def formatted_id(self):
        return f"E{self.eventID}" if self.eventID is not None else "Pending ID"

# Usage Example
if __name__ == "__main__":
    with SessionLocal() as session:
        event = session.query(Event).first()
        if event:
            print(event.formatted_id)  # Outputs 'E1', 'E2', etc.
        else:
            print("No event records found.")