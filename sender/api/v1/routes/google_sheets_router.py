from fastapi import APIRouter, Response

from schemas import GoogleSheetsUpdateTable, SuccessResponse, GoogleSheetsList, BadResponse
from services import get_lists, write_by_file_url
from settings import settings

router = APIRouter()


@router.get('/lists')
async def get_google_sheets_lists(response: Response) -> GoogleSheetsList | BadResponse:
    try:
        url = settings.API_CONFIG['url']
        name_list = get_lists(url)

        return GoogleSheetsList(name_list=name_list)
    except Exception:
        resp = BadResponse(text='Неправильный url или credential')
        response.status_code = resp.status

        return resp


@router.post('/update')
async def update_google_sheets(update_table_schema: GoogleSheetsUpdateTable, response: Response) -> SuccessResponse | BadResponse:
    try:
        config = settings.API_CONFIG
        write_by_file_url(update_table_schema.files, config, update_table_schema.list_name)

        return SuccessResponse()
    except:
        resp = BadResponse(text='Неправильные загруженные файлы, или неверно проставленные фильтры, или неверно выбран лист')
        response.status_code = resp.status

        return resp
