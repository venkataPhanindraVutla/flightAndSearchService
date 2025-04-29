from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.airport import AirportCreate, AirportUpdate, AirportOut
from app.services import airport as service_airport
from app.crud import airport as crud_airport

router = APIRouter(prefix="/airports", tags=["Airports"])

@router.post("/", response_model=AirportOut)
def create_airport(airport: AirportCreate, db: Session = Depends(get_db)):
    result = service_airport.create_new_airport(db, airport)
    if not result:
        raise HTTPException(status_code=500, detail="Airport creation failed")
    return result

@router.get("/{airport_id}", response_model=AirportOut)
def read_airport(airport_id: int, db: Session = Depends(get_db)):
    airport = crud_airport.get_airport(db, airport_id)
    if airport is None:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport

@router.put("/{airport_id}", response_model=AirportOut)
def update_airport(airport_id: int, airport: AirportUpdate, db: Session = Depends(get_db)):
    try:
        return service_airport.update_existing_airport(db, airport_id, airport)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{airport_id}")
def delete_airport(airport_id: int, db: Session = Depends(get_db)):
    success = crud_airport.delete_airport(db, airport_id)
    if not success:
        raise HTTPException(status_code=404, detail="Airport not found or already deleted")
    return {"message": "Airport deleted successfully"}
