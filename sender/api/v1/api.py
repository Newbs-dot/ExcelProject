from fastapi import APIRouter

from .routes import google_sheets_router

api_router = APIRouter(prefix='/v1')
api_router.include_router(google_sheets_router, tags=['google sheets'], prefix='/googleSheets')
