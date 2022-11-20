from fastapi import status
from pydantic import BaseModel


class SuccessResponse(BaseModel):
    status: str = status.HTTP_200_OK

    class Config:
        arbitrary_types_allowed = True
