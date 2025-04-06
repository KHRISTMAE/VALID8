from sqlalchemy.orm import Session
from Model import OfficerEvent
from schemas import OfficerEventCreate, OfficerEventUpdate

# Create a new OfficerEvent
def create_officer_event(db: Session, officer_event: OfficerEventCreate):
    db_officer_event = OfficerEvent(
        officerID=officer_event.officerID,
        eventID=officer_event.eventID
    )
    db.add(db_officer_event)
    db.commit()
    db.refresh(db_officer_event)
    return db_officer_event

# Get all OfficerEvents
def get_officer_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(OfficerEvent).offset(skip).limit(limit).all()

# Get an OfficerEvent by officerID and eventID
def get_officer_event(db: Session, officer_id: int, event_id: int):
    return db.query(OfficerEvent).filter(OfficerEvent.officerID == officer_id, OfficerEvent.eventID == event_id).first()

# Update an OfficerEvent by officerID and eventID
def update_officer_event(db: Session, officer_id: int, event_id: int, officer_event: OfficerEventUpdate):
    db_officer_event = db.query(OfficerEvent).filter(OfficerEvent.officerID == officer_id, OfficerEvent.eventID == event_id).first()
    if db_officer_event:
        for key, value in officer_event.dict(exclude_unset=True).items():
            setattr(db_officer_event, key, value)
        db.commit()
        db.refresh(db_officer_event)
        return db_officer_event
    return None

# Delete an OfficerEvent by officerID and eventID
def delete_officer_event(db: Session, officer_id: int, event_id: int):
    db_officer_event = db.query(OfficerEvent).filter(OfficerEvent.officerID == officer_id, OfficerEvent.eventID == event_id).first()
    if db_officer_event:
        db.delete(db_officer_event)
        db.commit()
        return db_officer_event
    return None
