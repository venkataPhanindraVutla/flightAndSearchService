from pydantic import BaseModel

class AirplaneBase(BaseModel):
    model_number: str
    capacity: int

class AirplaneCreate(AirplaneBase):
    pass

class AirplaneUpdate(AirplaneBase):
    pass

class AirplaneOut(AirplaneBase):
    id: int

    class Config:
        from_attributes = True
