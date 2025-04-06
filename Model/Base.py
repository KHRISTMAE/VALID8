from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example database setup
DATABASE_URL = "postgresql://postgres:ladyzoy@localhost/valid"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import all models here to register them with the Base
from Model.Event import Event
from Model.EventOrganizer import EventOrganizer
from Model.OfficerEvent import OfficerEvent
from Model.Program import Program
from Model.Role import Role
from Model.SSGOfficer import SSGOfficer
from Model.Student import Student
from Model.UserRoles import UserRoles
from Model.UserTable import UserTable

Base.metadata.create_all(bind=engine)
