from sqlalchemy.orm import Session
from Model import Program
from schemas import ProgramCreate, ProgramUpdate

# Create a new Program
def create_program(db: Session, program: ProgramCreate):
    db_program = Program(
        programName=program.programName,
        college=program.college
    )
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

# Get all Programs
def get_programs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Program).offset(skip).limit(limit).all()

# Get a Program by programID
def get_program(db: Session, program_id: int):
    return db.query(Program).filter(Program.programID == program_id).first()

# Update a Program by programID
def update_program(db: Session, program_id: int, program: ProgramUpdate):
    db_program = db.query(Program).filter(Program.programID == program_id).first()
    if db_program:
        for key, value in program.dict(exclude_unset=True).items():
            setattr(db_program, key, value)
        db.commit()
        db.refresh(db_program)
        return db_program
    return None

# Delete a Program by programID
def delete_program(db: Session, program_id: int):
    db_program = db.query(Program).filter(Program.programID == program_id).first()
    if db_program:
        db.delete(db_program)
        db.commit()
        return db_program
    return None
