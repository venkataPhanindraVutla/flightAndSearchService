from sqlalchemy.orm import Session
from app.db.schemas.airplane import AirplaneCreate, AirplaneUpdate
from app.crud import airplane as crud_airplane

def create_new_airplane(db: Session, airplane_in: AirplaneCreate):
    return crud_airplane.create_airplane(db, airplane_in)

def update_existing_airplane(db: Session, airplane_id: int, updates: AirplaneUpdate):
    airplane = crud_airplane.get_airplane(db, airplane_id)
    if not airplane:
        raise ValueError("Airplane not found")
    return crud_airplane.update_airplane(db, airplane, updates)
