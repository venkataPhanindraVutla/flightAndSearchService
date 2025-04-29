from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.models.airplane import Airplane
from app.db.schemas.airplane import AirplaneCreate, AirplaneUpdate

def get_airplane(db: Session, airplane_id: int):
    try:
        return db.query(Airplane).filter(Airplane.id == airplane_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching airplane: {e}")
        return None

def get_airplanes(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Airplane).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        print(f"Error fetching airplanes: {e}")
        return []

def create_airplane(db: Session, airplane: AirplaneCreate):
    try:
        db_airplane = Airplane(**airplane.dict())
        db.add(db_airplane)
        db.commit()
        db.refresh(db_airplane)
        return db_airplane
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating airplane: {e}")
        return None

def update_airplane(db: Session, db_airplane: Airplane, updates: AirplaneUpdate):
    try:
        for key, value in updates.dict().items():
            setattr(db_airplane, key, value)
        db.commit()
        db.refresh(db_airplane)
        return db_airplane
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating airplane: {e}")
        return None

def delete_airplane(db: Session, airplane_id: int):
    try:
        airplane = get_airplane(db, airplane_id)
        if airplane:
            db.delete(airplane)
            db.commit()
            return True
        return False
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting airplane: {e}")
        return False
