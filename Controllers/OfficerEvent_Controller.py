from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.OfficerEvent import OfficerEvent
from schemas.OfficerEvent_Schema import OfficerEventCreate, OfficerEventResponse
from Repository.OfficerEventRepository import OfficerEventRepository
from Database.database import get_db  # Dependency injection sa DB session

router = APIRouter(prefix="/officer-events", tags=["OfficerEvents"])

@router.post("/", response_model=OfficerEventResponse)
def create_officer_event(data: OfficerEventCreate, db: Session = Depends(get_db)):
    repo = OfficerEventRepository(db)
    new_record = OfficerEvent(officer_id=data.officer_id, event_id=data.event_id)
    created = repo.create(new_record)
    return created

@router.get("/", response_model=list[OfficerEventResponse])
def get_all_officer_events(db: Session = Depends(get_db)):
    repo = OfficerEventRepository(db)
    return repo.get_all()

@router.get("/{officer_id}/{event_id}", response_model=OfficerEventResponse)
def get_officer_event(officer_id: int, event_id: int, db: Session = Depends(get_db)):
    repo = OfficerEventRepository(db)
    record = repo.get_by_ids(officer_id, event_id)
    if not record:
        raise HTTPException(status_code=404, detail="OfficerEvent not found")
    return record

@router.delete("/{officer_id}/{event_id}")
def delete_officer_event(officer_id: int, event_id: int, db: Session = Depends(get_db)):
    repo = OfficerEventRepository(db)
    record = repo.get_by_ids(officer_id, event_id)
    if not record:
        raise HTTPException(status_code=404, detail="OfficerEvent not found")
    repo.delete(record)
    return {"message": "OfficerEvent deleted successfully"}
