from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_event, get_events, get_event_by_id, update_event, delete_event
from schemas import EventCreate, EventUpdate, EventResponse
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create an event
@router.post("/", response_model=EventResponse)
def create_event_route(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db=db, event=event)

# Get all events
@router.get("/", response_model=list[EventResponse])
def get_events_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_events(db=db, skip=skip, limit=limit)

# Get event by ID
@router.get("/{eventID}", response_model=EventResponse)
def get_event_by_id_route(eventID: int, db: Session = Depends(get_db)):
    db_event = get_event_by_id(db=db, eventID=eventID)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

# Update an event
@router.put("/{eventID}", response_model=EventResponse)
def update_event_route(eventID: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = update_event(db=db, eventID=eventID, event=event)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

# Delete an event
@router.delete("/{eventID}", response_model=EventResponse)
def delete_event_route(eventID: int, db: Session = Depends(get_db)):
    db_event = delete_event(db=db, eventID=eventID)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
