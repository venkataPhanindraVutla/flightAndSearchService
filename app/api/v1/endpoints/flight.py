from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.schemas.flight import FlightCreate, FlightUpdate, FlightOut
from app.services import flight as flight_service
from app.crud import flight as flight_crud

router = APIRouter(prefix="/flights", tags=["Flights"])

@router.post("/", response_model=FlightOut)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    try:
        return flight_service.create_new_flight(db, flight)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{flight_id}", response_model=FlightOut)
def read_flight(flight_id: int, db: Session = Depends(get_db)):
    db_flight = flight_crud.get_flight(db, flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight

@router.put("/{flight_id}", response_model=FlightOut)
def update_flight(flight_id: int, flight: FlightUpdate, db: Session = Depends(get_db)):
    try:
        return flight_service.update_existing_flight(db, flight_id, flight)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{flight_id}")
def delete_flight(flight_id: int, db: Session = Depends(get_db)):
    result = flight_crud.delete_flight(db, flight_id)
    if not result:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {"message": "Flight deleted successfully"}
