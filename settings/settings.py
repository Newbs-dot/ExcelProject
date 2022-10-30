import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    TG_BOT_TOKEN: str = os.getenv('TG_BOT_TOKEN')
    TG_API_ID: str = os.getenv('TG_API_ID')
    TG_API_HASH: str = os.getenv('TG_API_HASH')
    TG_SESSION_NAME: str = os.getenv('TG_SESSION_NAME')

    API_ROOT_URL: str = os.getenv('API_ROOT_URL')
    API_SECRET_KEY: str = os.getenv('API_SECRET_KEY')
    API_PROJECT_NAME: str = os.getenv('API_PROJECT_NAME')
    API_VERSION: str = os.getenv('API_VERSION')

    class Config:
        case_sensitive = True


load_dotenv()
settings = Settings()
