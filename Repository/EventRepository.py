from sqlalchemy.orm import Session # type: ignore
from Model.Event import Event

class EventRepository:

    def __init__(self, session: Session):
        self.session = session

    def find_all(self):
        return self.session.query(Event).all()

    def find_by_id(self, event_id: int):
        return self.session.query(Event).filter(Event.eventID == event_id).first()

    def save(self, event: Event):
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event

    def delete(self, event: Event):
        self.session.delete(event)
        self.session.commit()

    def find_by_event_name_containing(self, event_name: str):
        """Search events where eventName contains the provided string (case-insensitive)"""
        return self.session.query(Event).filter(Event.eventName.ilike(f"%{event_name}%")).all()
