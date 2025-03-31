# crud/ssg_officer.py
from sqlalchemy.orm import Session
from Model.SSGOfficer import SSGOfficer

def get_officer_by_email(db: Session, email: str):
    return db.query(SSGOfficer).filter(SSGOfficer.email == email).first()

def create_ssg_officer(db: Session, officer: SSGOfficer):
    db.add(officer)
    db.commit()
    db.refresh(officer)
    return officer

def get_all_officers(db: Session):
    return db.query(SSGOfficer).all()
