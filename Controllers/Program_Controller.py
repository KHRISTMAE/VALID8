from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_program, get_programs, get_program, update_program, delete_program
from schemas import ProgramCreate, ProgramUpdate, ProgramResponse
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new Program
@router.post("/createProgram", response_model=ProgramResponse)
def create_program_route(program: ProgramCreate, db: Session = Depends(get_db)):
    return create_program(db=db, program=program)

# Get all Programs
@router.get("/getProgram", response_model=list[ProgramResponse])
def get_programs_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_programs(db=db, skip=skip, limit=limit)

# Get a Program by programID
@router.get("/{programID}", response_model=ProgramResponse)
def get_program_route(programID: int, db: Session = Depends(get_db)):
    db_program = get_program(db=db, programID=programID)
    if db_program is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program

# Update a Program by programID
@router.put("/{programID}", response_model=ProgramResponse)
def update_program_route(programID: int, program: ProgramUpdate, db: Session = Depends(get_db)):
    db_program = update_program(db=db, programID=programID, program=program)
    if db_program is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program

# Delete a Program by programID
@router.delete("/{programID}", response_model=ProgramResponse)
def delete_program_route(programID: int, db: Session = Depends(get_db)):
    db_program = delete_program(db=db, programID=programID)
    if db_program is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program
