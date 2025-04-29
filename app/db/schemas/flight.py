from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str
    airplane_id: int
    departure_airport_id: int
    arrival_airport_id: int
    departure_time: datetime
    arrival_time: datetime
    price: int
    boarding_gate: str | None = None
    total_seats: int

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class FlightOut(FlightBase):
    id: int

    class Config:
        from_attributes = True
