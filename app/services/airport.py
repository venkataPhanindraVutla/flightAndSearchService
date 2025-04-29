from sqlalchemy.orm import Session
from app.db.schemas.airport import AirportCreate, AirportUpdate
from app.crud import airport as crud_airport

def create_new_airport(db: Session, airport_in: AirportCreate):
    return crud_airport.create_airport(db, airport_in)

def update_existing_airport(db: Session, airport_id: int, updates: AirportUpdate):
    airport = crud_airport.get_airport(db, airport_id)
    if not airport:
        raise ValueError("Airport not found")
    return crud_airport.update_airport(db, airport, updates)
