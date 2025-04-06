from fastapi import FastAPI, HTTPException, Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError
from fastapi.middleware.cors import CORSMiddleware
from Database.database import Base, SessionLocal, engine
from Database.auto_imports_model import import_all_models
from sqlalchemy.sql import text
from Database.database import get_db
from Database.seed import create_admin_user
import logging, time

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS setup for frontend (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update if your frontend runs on a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root route
@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}

# Test Database Connection during startup
@app.on_event("startup")
def startup():
    import_all_models()  # Load all model files
    Base.metadata.create_all(bind=engine)
    
    # Test the database connection
    try:
        # Create a session and connect to the database
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        # Test a simple query to check the connection
        db.execute(text("SELECT 1"))  # Simple query to test the connection
        db.commit()
        
        logger.info("Database connection successful! ✅")
        db.close()
    except OperationalError as e:
        logger.error(f"Error connecting to the database: {e}")
    finally:
        db.close()

@app.get("/api/hello")
def read_hello():
    return {"message": "Hi Engr. Maricon Denber 'Nonchalant' Gahisan"}

# Login Model
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

# Hardcoded user DB (for demo purposes)
users_db = {
    "admin@example.com": {
        "password": "password123",
        "roles": ["admin"],
        "token": "dummy-jwt-token-123"
    },
    "student@example.com": {
        "password": "student123",
        "roles": ["student"],
        "token": "dummy-jwt-token-456"
    },
    "ssg@example.com": {
        "password": "ssgpassword",
        "roles": ["ssg"],
        "token": "dummy-jwt-token-789"
    },
    "eventorganizer@example.com": {
        "password": "organizer123",
        "roles": ["event-organizer"],
        "token": "dummy-jwt-token-321"
    },
    "combo@example.com": {
        "password": "combo123",
        "roles": ["student", "ssg", "event-organizer"],
        "token": "dummy-jwt-token-combo"
    },
}

# Login endpoint
@app.post("/login")
async def login(request: LoginRequest):
    logger.info(f"Login request received for email: {request.email}")
    user = users_db.get(request.email)

    if user and user["password"] == request.password:
        logger.info(f"Login success for: {request.email}")
        return {
            "email": request.email,
            "roles": user["roles"],
            "token": user["token"]
        }

    logger.warning(f"Login failed for: {request.email}")
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Include controllers (you can add your own)
from Controllers import Program_Controller
from Controllers import Student_Controller
from Controllers import Attendance_Controller
from Controllers import SSGOfficer_Controller
from Controllers import Role_Controller
from Controllers import UserRoles_Controller
from Controllers import Event_Controller
from Controllers import EventOrganizer_Controller
from Controllers import OfficerEvent_Controller
from Controllers import UserTable_Controller

# Including all routers
app.include_router(Attendance_Controller.router)
app.include_router(Event_Controller.router)
app.include_router(Role_Controller.router)
app.include_router(EventOrganizer_Controller.router)
app.include_router(Program_Controller.router)
app.include_router(UserRoles_Controller.router)
app.include_router(Student_Controller.router)
app.include_router(UserTable_Controller.router)
app.include_router(SSGOfficer_Controller.router)
app.include_router(OfficerEvent_Controller.router)

