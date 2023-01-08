from fastapi import status
from pydantic import BaseModel


class BadResponse(BaseModel):
    status: str = status.HTTP_500_INTERNAL_SERVER_ERROR
    text: str

    class Config:
        arbitrary_types_allowed = True
