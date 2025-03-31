from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from Model.Program import Program
from schemas.Program_Schema import ProgramCreate
from fastapi import HTTPException, status

class ProgramRepository:
    
    @staticmethod
    def create_program(db: Session, program_data: ProgramCreate):
        try:
            # Create a new Program instance
            new_program = Program(
                programName=program_data.programName, 
                college=program_data.college
            )
            
            # Add the program to the session and commit
            db.add(new_program)
            db.commit()
            
            # Refresh to get the programID (auto-generated)
            db.refresh(new_program)
            
            # Return the new program with its programID
            return new_program
        
        except SQLAlchemyError as e:
            db.rollback()  # Rollback the transaction on error
            raise HTTPException(status_code=500, detail="Error creating program: " + str(e))

    @staticmethod
    def get_program_by_id(db: Session, program_id: int):
        program = db.query(Program).filter(Program.programID == program_id).first()
        if not program:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Program not found")
        return program

    @staticmethod
    def get_all_programs(db: Session):
        programs = db.query(Program).all()
        return programs

    @staticmethod
    def update_program(db: Session, program_id: int, program_data: ProgramCreate):
        program = db.query(Program).filter(Program.programID == program_id).first()
        if not program:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Program not found")

        # Update the program fields
        program.programName = program_data.programName
        program.college = program_data.college
        
        # Commit the changes and refresh to update the object with new data
        db.commit()
        db.refresh(program)
        
        return program

    @staticmethod
    def delete_program(db: Session, program_id: int):
        program = db.query(Program).filter(Program.programID == program_id).first()
        if not program:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Program not found")
        
        db.delete(program)
        db.commit()
        return {"message": "Program deleted successfully"}
