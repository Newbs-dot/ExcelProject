from fastapi import APIRouter, status, Request

from services import get_data_from_file, write_data_by_url

router = APIRouter()
file = 'D:\Code\PythonExcelBot\Orgs\Org1.xlsx'


@router.post('/write', status_code=status.HTTP_200_OK)
async def write_data(request: Request) -> None:
    data = await get_data_from_file(file)
    await write_data_by_url(
        'https://docs.google.com/spreadsheets/d/1NdTjc7iLh1YcdVwLbfyFSbh9m_8VTjW8YZlS8lMyOXY/edit#gid=1198610154',
        data)

    return 'OK'
