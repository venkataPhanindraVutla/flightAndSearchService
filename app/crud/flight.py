from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.models.flight import Flight
from app.db.schemas.flight import FlightCreate, FlightUpdate

def get_flight(db: Session, flight_id: int):
    try:
        return db.query(Flight).filter(Flight.id == flight_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching flight: {e}")
        return None

def get_flight_by_number(db: Session, number: str):
    try:
        return db.query(Flight).filter(Flight.flight_number == number).first()
    except SQLAlchemyError as e:
        print(f"Error fetching flight by number: {e}")
        return None

def get_flights(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Flight).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        print(f"Error fetching flights: {e}")
        return []

def create_flight(db: Session, flight_in: FlightCreate):
    try:
        flight = Flight(**flight_in.dict())
        db.add(flight)
        db.commit()
        db.refresh(flight)
        return flight
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating flight: {e}")
        return None

def update_flight(db: Session, db_flight: Flight, flight_update: FlightUpdate):
    try:
        for key, value in flight_update.dict().items():
            setattr(db_flight, key, value)
        db.commit()
        db.refresh(db_flight)
        return db_flight
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating flight: {e}")
        return None

def delete_flight(db: Session, flight_id: int):
    try:
        flight = get_flight(db, flight_id)
        if flight:
            db.delete(flight)
            db.commit()
            return True
        return False
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting flight: {e}")
        return False
