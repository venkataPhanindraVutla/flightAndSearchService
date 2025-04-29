# app/main.py

from fastapi import FastAPI
from app.api.v1.api_router import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Airline Microservice ✈️"}
