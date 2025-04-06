from sqlalchemy.orm import Session
from Model import SSGOfficer
from schemas import SSGOfficerCreate, SSGOfficerUpdate

# Create a new SSGOfficer
def create_ssg_officer(db: Session, officer: SSGOfficerCreate):
    db_officer = SSGOfficer(
        name=officer.name,
        position=officer.position,
        email=officer.email,
        password=officer.password  # This will be hashed in the model
    )
    db.add(db_officer)
    db.commit()
    db.refresh(db_officer)
    return db_officer

# Get all SSGOfficers
def get_ssg_officers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(SSGOfficer).offset(skip).limit(limit).all()

# Get an SSGOfficer by officerID
def get_ssg_officer(db: Session, officer_id: int):
    return db.query(SSGOfficer).filter(SSGOfficer.officerID == officer_id).first()

# Update an SSGOfficer's details
def update_ssg_officer(db: Session, officer_id: int, officer: SSGOfficerUpdate):
    db_officer = db.query(SSGOfficer).filter(SSGOfficer.officerID == officer_id).first()
    if db_officer:
        for key, value in officer.dict(exclude_unset=True).items():
            setattr(db_officer, key, value)
        db.commit()
        db.refresh(db_officer)
        return db_officer
    return None

# Delete an SSGOfficer by officerID
def delete_ssg_officer(db: Session, officer_id: int):
    db_officer = db.query(SSGOfficer).filter(SSGOfficer.officerID == officer_id).first()
    if db_officer:
        db.delete(db_officer)
        db.commit()
        return db_officer
    return None
