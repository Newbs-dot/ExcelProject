from fastapi import APIRouter, status

router = APIRouter()


@router.post('/auth', status_code=status.HTTP_200_OK)
async def auth():
    return {'status': status.HTTP_200_OK}
