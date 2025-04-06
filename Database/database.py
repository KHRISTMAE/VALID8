from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:ladyzoy@localhost/ABCC"  # i-edit sa imo actual DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# I-export kini para magamit sa controller
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
