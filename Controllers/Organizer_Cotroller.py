from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.EventOrganizer import EventOrganizer  # Assuming this is your model path
from pydantic import BaseModel

router = APIRouter(prefix="/organizers", tags=["Event Organizers"])

class OrganizerCreate(BaseModel):
    organizerName: str
    email: str
    password: str

class OrganizerLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_organizer(data: OrganizerCreate, db: Session = Depends(get_db)):
    existing = db.query(EventOrganizer).filter(EventOrganizer.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_organizer = EventOrganizer(
        organizerName=data.organizerName,
        email=data.email,
        password=data.password
    )
    db.add(new_organizer)
    db.commit()
    db.refresh(new_organizer)
    return {"message": "Organizer registered successfully", "organizerID": new_organizer.organizerID}

@router.post("/login")
def login_organizer(data: OrganizerLogin, db: Session = Depends(get_db)):
    organizer = db.query(EventOrganizer).filter(EventOrganizer.email == data.email).first()
    if not organizer or not organizer.check_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "organizerID": organizer.organizerID}
