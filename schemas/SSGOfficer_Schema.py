from pydantic import BaseModel

# Base schema for common fields
class SSGOfficerBase(BaseModel):
    name: str
    position: str
    email: str
    
# Create schema for creating new SSGOfficer
class SSGOfficerCreate(SSGOfficerBase):
    password: str  # Required to create an officer, will be hashed

# Update schema for updating an existing officer's information (except password)
class SSGOfficerUpdate(SSGOfficerBase):
    pass

# Response schema for returning officer information
class SSGOfficerResponse(SSGOfficerBase):
    officerID: int
    formatted_id: str

    class Config:
        from_attributes = True  # This tells Pydantic to treat SQLAlchemy models as dicts
