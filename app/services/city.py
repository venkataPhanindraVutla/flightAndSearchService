# app/services/city.py

from sqlalchemy.orm import Session
from app.db.schemas.city import CityCreate, CityUpdate
from app.crud import city as city_crud

def create_new_city(city_in: CityCreate, db: Session):
    existing = city_crud.get_city_by_name(db, city_in.name)
    if existing:
        raise ValueError("City with this name already exists.")
    return city_crud.create_city(db, city_in)

def get_city_by_id(city_id: int, db: Session):
    return city_crud.get_city(db, city_id)

def get_all_cities(skip: int, limit: int, db: Session):
    return city_crud.get_cities(db, skip, limit)

def update_existing_city(city_id: int, city_in: CityUpdate, db: Session):
    db_city = city_crud.get_city(db, city_id)
    if not db_city:
        return None
    return city_crud.update_city(db, db_city, city_in)

def delete_existing_city(city_id: int, db: Session):
    return city_crud.delete_city(db, city_id)
