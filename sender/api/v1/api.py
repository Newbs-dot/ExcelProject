from fastapi import APIRouter
from .routes import document_router, google_doc_router

api_router = APIRouter(prefix='/v1')
api_router.include_router(document_router, tags=['document'])
api_router.include_router(google_doc_router, tags=['google doc'])
