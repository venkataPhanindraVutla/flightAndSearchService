from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.schemas.airplane import AirplaneCreate, AirplaneUpdate, AirplaneOut
from app.services import airplane as service_airplane
from app.crud import airplane as crud_airplane

router = APIRouter(prefix="/airplanes", tags=["Airplanes"])

@router.post("/", response_model=AirplaneOut)
def create_airplane(airplane: AirplaneCreate, db: Session = Depends(get_db)):
    result = service_airplane.create_new_airplane(db, airplane)
    if not result:
        raise HTTPException(status_code=500, detail="Airplane creation failed")
    return result

@router.get("/{airplane_id}", response_model=AirplaneOut)
def read_airplane(airplane_id: int, db: Session = Depends(get_db)):
    airplane = crud_airplane.get_airplane(db, airplane_id)
    if not airplane:
        raise HTTPException(status_code=404, detail="Airplane not found")
    return airplane

@router.put("/{airplane_id}", response_model=AirplaneOut)
def update_airplane(airplane_id: int, airplane: AirplaneUpdate, db: Session = Depends(get_db)):
    try:
        return service_airplane.update_existing_airplane(db, airplane_id, airplane)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{airplane_id}")
def delete_airplane(airplane_id: int, db: Session = Depends(get_db)):
    success = crud_airplane.delete_airplane(db, airplane_id)
    if not success:
        raise HTTPException(status_code=404, detail="Airplane not found or already deleted")
    return {"message": "Airplane deleted successfully"}
