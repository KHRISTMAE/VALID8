from sqlalchemy.orm import Session
from Model import EventOrganizer
from schemas import EventOrganizerCreate, EventOrganizerUpdate

# Create an event organizer
def create_event_organizer(db: Session, event_organizer: EventOrganizerCreate):
    db_event_organizer = EventOrganizer(
        organizerName=event_organizer.organizerName,
        email=event_organizer.email,
        password=event_organizer.password  # The `set_password` method will hash it
    )
    db.add(db_event_organizer)
    db.commit()
    db.refresh(db_event_organizer)
    return db_event_organizer

# Get all event organizers
def get_event_organizers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EventOrganizer).offset(skip).limit(limit).all()

# Get an event organizer by ID
def get_event_organizer_by_id(db: Session, organizer_id: int):
    return db.query(EventOrganizer).filter(EventOrganizer.organizerID == organizer_id).first()

# Update an event organizer
def update_event_organizer(db: Session, organizer_id: int, event_organizer: EventOrganizerUpdate):
    db_event_organizer = db.query(EventOrganizer).filter(EventOrganizer.organizerID == organizer_id).first()
    if db_event_organizer:
        for key, value in event_organizer.dict(exclude_unset=True).items():
            setattr(db_event_organizer, key, value)
        db.commit()
        db.refresh(db_event_organizer)
        return db_event_organizer
    return None

# Delete an event organizer
def delete_event_organizer(db: Session, organizer_id: int):
    db_event_organizer = db.query(EventOrganizer).filter(EventOrganizer.organizerID == organizer_id).first()
    if db_event_organizer:
        db.delete(db_event_organizer)
        db.commit()
        return db_event_organizer
    return None
