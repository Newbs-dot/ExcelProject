import base64
import json

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import configs_repository
from database import get_db
from sender.models import SuccessResponse, GoogleSheetsUpdateTable
from services import google_sheets_service,write_by_file_url

router = APIRouter()


@router.post('/updateTable')
async def update_table(update_table_schema: GoogleSheetsUpdateTable, db: Session = Depends(get_db)):
    file_id = google_sheets_service.get_file_id_by_url(update_table_schema.url)
    if file_id is None:
        raise HTTPException(status_code=402, detail='Invalid google table url')

    config = configs_repository.get_config_by_id(db, update_table_schema.url)
    decoded_bytes = base64.b64decode(config.file)
    decoded_str = decoded_bytes.decode('utf-8')
    json_str = json.loads(decoded_str)

    write_by_file_url(update_table_schema.url, update_table_schema.files, json_str)

    return SuccessResponse()
