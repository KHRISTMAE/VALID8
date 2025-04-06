from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_officer_event, get_officer_events, get_officer_event, update_officer_event, delete_officer_event
from schemas import OfficerEventCreate, OfficerEventUpdate, OfficerEventResponse
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new OfficerEvent
@router.post("/", response_model=OfficerEventResponse)
def create_officer_event_route(officer_event: OfficerEventCreate, db: Session = Depends(get_db)):
    return create_officer_event(db=db, officer_event=officer_event)

# Get all OfficerEvents
@router.get("/", response_model=list[OfficerEventResponse])
def get_officer_events_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_officer_events(db=db, skip=skip, limit=limit)

# Get an OfficerEvent by officerID and eventID
@router.get("/{officerID}/{eventID}", response_model=OfficerEventResponse)
def get_officer_event_route(officerID: int, eventID: int, db: Session = Depends(get_db)):
    db_officer_event = get_officer_event(db=db, officerID=officerID, eventID=eventID)
    if db_officer_event is None:
        raise HTTPException(status_code=404, detail="OfficerEvent not found")
    return db_officer_event

# Update an OfficerEvent by officerID and eventID
@router.put("/{officerID}/{eventID}", response_model=OfficerEventResponse)
def update_officer_event_route(officerID: int, eventID: int, officer_event: OfficerEventUpdate, db: Session = Depends(get_db)):
    db_officer_event = update_officer_event(db=db, officerID=officerID, eventID=eventID, officer_event=officer_event)
    if db_officer_event is None:
        raise HTTPException(status_code=404, detail="OfficerEvent not found")
    return db_officer_event

# Delete an OfficerEvent by officerID and eventID
@router.delete("/{officerID}/{eventID}", response_model=OfficerEventResponse)
def delete_officer_event_route(officerID: int, eventID: int, db: Session = Depends(get_db)):
    db_officer_event = delete_officer_event(db=db, officerID=officerID, eventID=eventID)
    if db_officer_event is None:
        raise HTTPException(status_code=404, detail="OfficerEvent not found")
    return db_officer_event
