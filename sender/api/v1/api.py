from fastapi import APIRouter

from .routes import google_doc_router, google_router, filters_router, users_router

api_router = APIRouter(prefix='/v1')
api_router.include_router(google_doc_router, tags=['google document'], prefix='/googleDoc')
api_router.include_router(google_router, tags=['google'], prefix='/google')
api_router.include_router(filters_router, tags=['filters'], prefix='/filters')
api_router.include_router(users_router, tags=['users'], prefix='/users')
