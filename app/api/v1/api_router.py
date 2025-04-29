from fastapi import APIRouter
from app.api.v1.endpoints import city

api_router = APIRouter()
api_router.include_router(city.router, prefix="/cities", tags=["Cities"])
api_router.include_router(city.router, prefix="/airports", tags=["Airports"])
api_router.include_router(city.router, prefix="/airplanes", tags=["Airplanes"])
api_router.include_router(city.router, prefix="/flights", tags=["Flights"])
