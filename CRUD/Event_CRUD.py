from sqlalchemy.orm import Session
from Model import Event
from schemas.Event_Schema import EventCreate, EventUpdate

def create_event(self, event: EventCreate):
    db_event = Event(**event.dict())
    self.db.add(db_event)
    self.db.commit()
    self.db.refresh(db_event)
    return db_event

def get_events(self, skip: int = 0, limit: int = 10):
    return self.db.query(Event).offset(skip).limit(limit).all()

def get_event_by_id(self, event_id: int):
    return self.db.query(Event).filter(Event.eventID == event_id).first()

def update_event(self, event_id: int, event: EventUpdate):
    db_event = self.db.query(Event).filter(Event.eventID == event_id).first()
    if db_event:
        for key, value in event.dict(exclude_unset=True).items():
            setattr(db_event, key, value)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event
    return None

def delete_event(self, event_id: int):
    db_event = self.db.query(Event).filter(Event.eventID == event_id).first()
    if db_event:
        self.db.delete(db_event)
        self.db.commit()
        return db_event
    return None
