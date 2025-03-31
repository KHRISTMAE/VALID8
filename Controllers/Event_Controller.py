from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.Event import Event
from schemas import EventCreate, EventResponse

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

# Create Event
@router.post("/create", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        eventName=event.eventName,
        dateAndTime=event.dateAndTime,
        location=event.location,
        organizerID=event.organizerID
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Get All Events
@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events

# Get Single Event
@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.eventID == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Delete Event
@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.eventID == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}