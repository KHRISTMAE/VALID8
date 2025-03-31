from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..Database import database
from .. import models

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users(db: Session = Depends(database.get_db)):
    return db.query(models.User).all()
