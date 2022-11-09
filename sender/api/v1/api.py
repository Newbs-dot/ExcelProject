from fastapi import APIRouter

from .routes import google_doc_router

api_router = APIRouter(prefix='/v1')
api_router.include_router(google_doc_router, tags=['google document'])
