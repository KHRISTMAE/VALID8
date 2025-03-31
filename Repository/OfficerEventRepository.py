from sqlalchemy.orm import Session
from Model.OfficerEvent import OfficerEvent

class OfficerEventRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[OfficerEvent]:
        return self.db.query(OfficerEvent).all()

    def get_by_ids(self, officer_id: int, event_id: int) -> OfficerEvent | None:
        return self.db.query(OfficerEvent).filter(
            OfficerEvent.officer_id == officer_id,
            OfficerEvent.event_id == event_id
        ).first()

    def create(self, officer_event: OfficerEvent) -> OfficerEvent:
        self.db.add(officer_event)
        self.db.commit()
        self.db.refresh(officer_event)
        return officer_event

    def delete(self, officer_event: OfficerEvent):
        self.db.delete(officer_event)
        self.db.commit()
