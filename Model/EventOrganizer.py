from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal
import bcrypt

class EventOrganizer(Base):
    __tablename__ = 'event_organizer'
    
    organizerID = Column(Integer, primary_key=True, autoincrement=True)
    organizerName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Hashed password
    
    # Define relationship to Event using string reference
    event_list = relationship('Event', back_populates='event_organizer')
    
    def __init__(self, organizerName, email, password):
        self.organizerName = organizerName
        self.email = email
        self.set_password(password)
    
    def set_password(self, plain_password):
        """Hashes and sets the password."""
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')  # Store as string
    
    def check_password(self, plain_password):
        """Verifies a plain password against the stored hashed password."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))
    
    def __repr__(self):
        return f"<EventOrganizer(organizerID={self.organizerID}, organizerName='{self.organizerName}')>"
    
    @property
    def formatted_id(self):
        """Returns formatted organizer ID."""
        return f"O{self.organizerID}" if self.organizerID is not None else "Pending ID"

# Encapsulating session handling in a function
def fetch_first_event_organizer():
    """Fetches the first event organizer and prints the formatted ID."""
    with SessionLocal() as session:
        event_organizer = session.query(EventOrganizer).first()
        if event_organizer:
            print(event_organizer.formatted_id)  # Outputs 'O1', 'O2', etc.
        else:
            print("No event organizer records found.")