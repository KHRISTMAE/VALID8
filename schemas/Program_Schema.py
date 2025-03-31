from pydantic import BaseModel, Field

class ProgramBase(BaseModel):
    programName: str = Field(..., example="Computer Science")

class ProgramCreate(ProgramBase):
    college: str  # Only need to define college, programName is inherited

class ProgramResponse(ProgramBase):
    id: int  # The ID returned in the response, could be `programID`

    class Config:
        from_attributes = True  # Allows ORM models to be returned directly
