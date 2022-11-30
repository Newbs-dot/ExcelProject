from fastapi import APIRouter, HTTPException

from sender.models import GoogleSheetsUpdateTable
from services import filter_service, google_sheets_service

router = APIRouter()


@router.post('/updateTable')
async def update_table(update_table_schema: GoogleSheetsUpdateTable):
    if not filter_service.check_filter_type(update_table_schema.filters):
        raise HTTPException(status_code=401, detail='Invalid filters in request')
    file_id = google_sheets_service.get_file_id_by_url(update_table_schema.url)
    if file_id is None:
        raise HTTPException(status_code=402, detail='Invalid google table url')

    return {"Uploaded Files:": "asasdas"}
