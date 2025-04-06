from pydantic import BaseModel

# Base schema for common fields
class RoleBase(BaseModel):
    role_name: str

# Create schema: For creating a new Role
class RoleCreate(RoleBase):
    pass

# Update schema: For updating an existing Role
class RoleUpdate(RoleBase):
    pass

# Response schema: For returning Role data
class RoleResponse(RoleBase):
    roleID: int

    class Config:
        from_attributes = True  # This allows SQLAlchemy ORM models to be used
