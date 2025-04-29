from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Airplane(Base):
    __tablename__ = "airplanes"

    id = Column(Integer, primary_key=True, index=True)
    model_number = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False, default=200)
