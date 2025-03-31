from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.SSGOfficer import SSGOfficer
from schemas.SSGOfficer_Schema import SSGOfficerCreate, SSGOfficerLogin, SSGOfficerResponse

router = APIRouter(prefix="/ssg-officers", tags=["SSG Officers"])

@router.post("/register", response_model=SSGOfficerResponse)
def register_officer(data: SSGOfficerCreate, db: Session = Depends(get_db)):
    existing = db.query(SSGOfficer).filter(SSGOfficer.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")

    new_officer = SSGOfficer(
        name=data.name,
        position=data.position,
        email=data.email,
        password=data.password
    )
    db.add(new_officer)
    db.commit()
    db.refresh(new_officer)
    return new_officer

@router.post("/login")
def login_officer(data: SSGOfficerLogin, db: Session = Depends(get_db)):
    officer = db.query(SSGOfficer).filter(SSGOfficer.email == data.email).first()
    if not officer or not officer.check_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {
        "message": "Login successful",
        "officerID": officer.officerID,
        "name": officer.name,
        "position": officer.position
    }

@router.get("/", response_model=list[SSGOfficerResponse])
def get_all_officers(db: Session = Depends(get_db)):
    officers = db.query(SSGOfficer).all()
    return officers
