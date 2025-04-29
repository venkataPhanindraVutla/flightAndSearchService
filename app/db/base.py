# app/db/base.py
#
# from app.db.models.airplane import Airplane
# from app.db.models.airport import Airport
# from app.db.models.city import City
# from app.db.models.flight import Flight

# Needed for Alembic to recognize models
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
