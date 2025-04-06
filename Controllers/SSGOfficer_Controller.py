from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_ssg_officer, get_ssg_officers, get_ssg_officer, update_ssg_officer, delete_ssg_officer
from schemas import SSGOfficerCreate, SSGOfficerUpdate, SSGOfficerResponse
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new officer
@router.post("/", response_model=SSGOfficerResponse)
def create_officer_route(officer: SSGOfficerCreate, db: Session = Depends(get_db)):
    return create_ssg_officer(db=db, officer=officer)

# Get all officers
@router.get("/", response_model=list[SSGOfficerResponse])
def get_officers_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_ssg_officers(db=db, skip=skip, limit=limit)

# Get officer by officerID
@router.get("/{officerID}", response_model=SSGOfficerResponse)
def get_officer_route(officerID: int, db: Session = Depends(get_db)):
    db_officer = get_ssg_officer(db=db, officerID=officerID)
    if db_officer is None:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer

# Update officer details
@router.put("/{officerID}", response_model=SSGOfficerResponse)
def update_officer_route(officerID: int, officer: SSGOfficerUpdate, db: Session = Depends(get_db)):
    db_officer = update_ssg_officer(db=db, officerID = officerID, officer=officer)
    if db_officer is None:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer

# Delete officer by officerID
@router.delete("/{officerID}", response_model=SSGOfficerResponse)
def delete_officer_route(officerID: int, db: Session = Depends(get_db)):
    db_officer = delete_ssg_officer(db=db, officerID=officerID)
    if db_officer is None:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer
