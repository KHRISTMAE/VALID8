from sqlalchemy.orm import Session
from Model.EventOrganizer import EventOrganizer

class EventOrganizerRepository:

    def __init__(self, session: Session):
        self.session = session

    def find_all(self):
        return self.session.query(EventOrganizer).all()

    def find_by_id(self, organizer_id: int):
        return self.session.query(EventOrganizer).filter(EventOrganizer.organizerID == organizer_id).first()

    def save(self, organizer: EventOrganizer):
        self.session.add(organizer)
        self.session.commit()
        self.session.refresh(organizer)
        return organizer

    def delete(self, organizer: EventOrganizer):
        self.session.delete(organizer)
        self.session.commit()

    def find_by_organizer_name(self, organizer_name: str):
        """Find EventOrganizer by exact organizerName"""
        return self.session.query(EventOrganizer).filter(EventOrganizer.organizerName == organizer_name).first()
