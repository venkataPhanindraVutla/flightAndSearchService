from sqlalchemy.orm import Session
from app.db.schemas.flight import FlightCreate, FlightUpdate
from app.crud import flight as flight_crud

def create_new_flight(db: Session, flight_in: FlightCreate):
    existing = flight_crud.get_flight_by_number(db, flight_in.flight_number)
    if existing:
        raise ValueError("Flight with this number already exists.")
    return flight_crud.create_flight(db, flight_in)

def update_existing_flight(db: Session, flight_id: int, flight_update: FlightUpdate):
    db_flight = flight_crud.get_flight(db, flight_id)
    if not db_flight:
        raise ValueError("Flight not found.")
    return flight_crud.update_flight(db, db_flight, flight_update)
