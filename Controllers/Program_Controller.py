from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from fastapi import APIRouter
from Repository.ProgramRepository import ProgramRepository
from schemas.Program_Schema import ProgramCreate, ProgramResponse

router = APIRouter(prefix="/programs", tags=["Programs"])

@router.post("/", response_model=ProgramResponse)
def create_program(program: ProgramCreate, db: Session = Depends(get_db)):
    return ProgramRepository.create_program(db, program)

@router.get("/{program_id}", response_model=ProgramResponse)
def get_program(program_id: int, db: Session = Depends(get_db)):
    program = ProgramRepository.get_program_by_id(db, program_id)
    if program is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return program

@router.get("/", response_model=list[ProgramResponse])
def get_all_programs(db: Session = Depends(get_db)):
    return ProgramRepository.get_all_programs(db)

@router.put("/{program_id}", response_model=ProgramResponse)
def update_program(program_id: int, program: ProgramCreate, db: Session = Depends(get_db)):
    return ProgramRepository.update_program(db, program_id, program)

@router.delete("/{program_id}")
def delete_program(program_id: int, db: Session = Depends(get_db)):
    ProgramRepository.delete_program(db, program_id)
    return {"message": "Program deleted successfully"}
