# app/crud/city.py
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.db.models.city import City
from app.db.schemas.city import CityCreate, CityUpdate

def get_city(db: Session, city_id: int) -> City | None:
    try:
        return db.query(City).filter(City.id == city_id).first()
    except SQLAlchemyError as e:
        print(f"Error in get_city: {e}")
        return None

def get_city_by_name(db: Session, name: str) -> City | None:
    try:
        return db.query(City).filter(City.name == name).first()
    except SQLAlchemyError as e:
        print(f"Error in get_city_by_name: {e}")
        return None

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(City).offset(skip).limit(limit).all()

def create_city(db: Session, city: CityCreate):
    db_city = City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def update_city(db: Session, db_city: City, update_data: CityUpdate):
    db_city.name = update_data.name
    db.commit()
    db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)
    if db_city:
        db.delete(db_city)
        db.commit()
        return True
    return False
