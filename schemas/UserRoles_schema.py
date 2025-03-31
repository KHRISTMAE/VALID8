from pydantic import BaseModel

# Schema for creating a UserRole
class UserRolesCreate(BaseModel):
    userID: int
    roleID: int

# Schema for updating a UserRole
class UserRolesUpdate(BaseModel):
    userID: int
    roleID: int

# Schema for response
class UserRolesResponse(BaseModel):
    id: int
    userID: int
    roleID: int

    class Config:
        from_attributes = True
