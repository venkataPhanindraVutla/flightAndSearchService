from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.models.airport import Airport
from app.db.schemas.airport import AirportCreate, AirportUpdate

def get_airport(db: Session, airport_id: int):
    try:
        return db.query(Airport).filter(Airport.id == airport_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching airport: {e}")
        return None

def get_airports(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Airport).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        print(f"Error fetching airports: {e}")
        return []

def create_airport(db: Session, airport: AirportCreate):
    try:
        db_airport = Airport(**airport.dict())
        db.add(db_airport)
        db.commit()
        db.refresh(db_airport)
        return db_airport
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating airport: {e}")
        return None

def update_airport(db: Session, db_airport: Airport, updates: AirportUpdate):
    try:
        for key, value in updates.dict().items():
            setattr(db_airport, key, value)
        db.commit()
        db.refresh(db_airport)
        return db_airport
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating airport: {e}")
        return None

def delete_airport(db: Session, airport_id: int):
    try:
        airport = get_airport(db, airport_id)
        if airport:
            db.delete(airport)
            db.commit()
            return True
        return False
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting airport: {e}")
        return False
