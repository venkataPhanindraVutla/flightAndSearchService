# app/api/v1/endpoints/city.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.schemas.city import CityCreate, CityOut, CityUpdate
from app.services import city as city_service

router = APIRouter()

@router.post("/", response_model=CityOut)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    try:
        return city_service.create_new_city(city, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{city_id}", response_model=CityOut)
def read_city(city_id: int, db: Session = Depends(get_db)):
    city = city_service.get_city_by_id(city_id, db)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/", response_model=list[CityOut])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return city_service.get_all_cities(skip, limit, db)

@router.put("/{city_id}", response_model=CityOut)
def update_city(city_id: int, city: CityUpdate, db: Session = Depends(get_db)):
    updated = city_service.update_existing_city(city_id, city, db)
    if not updated:
        raise HTTPException(status_code=404, detail="City not found")
    return updated

@router.delete("/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    success = city_service.delete_existing_city(city_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="City not found")
    return {"ok": True, "message": "City deleted successfully"}
