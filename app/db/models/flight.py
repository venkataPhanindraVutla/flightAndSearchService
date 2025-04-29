from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, nullable=False)
    airplane_id = Column(Integer, ForeignKey("airplanes.id"), nullable=False)
    departure_airport_id = Column(Integer, ForeignKey("airports.id"), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey("airports.id"), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    price = Column(Integer, nullable=False)
    boarding_gate = Column(String, nullable=True)
    total_seats = Column(Integer, nullable=False)
