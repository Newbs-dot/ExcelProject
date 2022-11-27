from fastapi import APIRouter

from .routes import filters_router, users_router, google_sheets_router

api_router = APIRouter(prefix='/v1')
api_router.include_router(filters_router, tags=['filters'], prefix='/filters')
api_router.include_router(users_router, tags=['users'], prefix='/users')
api_router.include_router(google_sheets_router, tags=['google sheets'], prefix='/googleSheets')
