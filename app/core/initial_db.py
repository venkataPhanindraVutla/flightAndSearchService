# app/core/init_db.py

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import base

def init_db() -> None:
    db: Session = SessionLocal()
    try:
        # You can add default data here if needed
        pass
    finally:
        db.close()
