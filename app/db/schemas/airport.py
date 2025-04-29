from pydantic import BaseModel

class AirportBase(BaseModel):
    name: str
    address: str | None = None
    city_id: int

class AirportCreate(AirportBase):
    pass

class AirportUpdate(AirportBase):
    pass

class AirportOut(AirportBase):
    id: int

    class Config:
        from_attributes = True
