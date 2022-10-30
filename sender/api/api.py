from fastapi import APIRouter
from sender.api.routes import router

api_router = APIRouter()
api_router.include_router(router, tags=['hello'])
