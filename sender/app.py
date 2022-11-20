from fastapi import FastAPI

from api import api_router_v1
from database import Base, engine
from settings import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.API_PROJECT_NAME,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
)

app.include_router(api_router_v1, prefix=f'{settings.API_PREFIX}')
