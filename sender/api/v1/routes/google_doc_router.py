from fastapi import APIRouter, status
from models import DocumentWriteRequest

router = APIRouter()


@router.post('/googleDoc/write', status_code=status.HTTP_200_OK)
async def write_data_by_url(write_request_model: DocumentWriteRequest) -> None:
    print(write_request_model)
    return
