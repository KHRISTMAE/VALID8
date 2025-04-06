from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_event_organizer, get_event_organizers, get_event_organizer_by_id, update_event_organizer, delete_event_organizer
from schemas import EventOrganizerCreate, EventOrganizerUpdate, EventOrganizerResponse, EventOrganizerBase
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new event organizer
@router.post("/", response_model=EventOrganizerResponse)
def create_event_organizer_route(event_organizer: EventOrganizerCreate, db: Session = Depends(get_db)):
    return create_event_organizer(db=db, event_organizer=event_organizer)

# Get all event organizers
@router.get("/", response_model=list[EventOrganizerResponse])
def get_event_organizers_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_event_organizers(db=db, skip=skip, limit=limit)

# Get an event organizer by ID
@router.get("/{organizerID}", response_model=EventOrganizerResponse)
def get_event_organizer_by_id_route(organizerID: int, db: Session = Depends(get_db)):
    db_event_organizer = get_event_organizer_by_id(db=db, organizerID=organizerID)
    if db_event_organizer is None:
        raise HTTPException(status_code=404, detail="Event Organizer not found")
    return db_event_organizer

# Update an event organizer by ID
@router.put("/{organizerID}", response_model=EventOrganizerResponse)
def update_event_organizer_route(organizerID: int, event_organizer: EventOrganizerUpdate, db: Session = Depends(get_db)):
    db_event_organizer = update_event_organizer(db=db, organizerID=organizerID, event_organizer=event_organizer)
    if db_event_organizer is None:
        raise HTTPException(status_code=404, detail="Event Organizer not found")
    return db_event_organizer

# Delete an event organizer by ID
@router.delete("/{organizerID}", response_model=EventOrganizerResponse)
def delete_event_organizer_route(organizerID: int, db: Session = Depends(get_db)):
    db_event_organizer = delete_event_organizer(db=db, organizerID=organizerID)
    if db_event_organizer is None:
        raise HTTPException(status_code=404, detail="Event Organizer not found")
    return db_event_organizer
