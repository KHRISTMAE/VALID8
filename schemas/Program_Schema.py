from pydantic import BaseModel


# Base schema for common fields
class ProgramBase(BaseModel):
    programName: str
    college: str

# Create schema: For creating a new Program
class ProgramCreate(ProgramBase):
    pass

# Update schema: For updating an existing Program
class ProgramUpdate(ProgramBase):
    pass

# Response schema: For returning Program data
class ProgramResponse(ProgramBase):
    programID: str

    class Config:
        from_attributes = True  # This allows SQLAlchemy ORM models to be used
