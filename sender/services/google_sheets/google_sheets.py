import base64
import time

from sender.models import GoogleSheetsFilterItem
from services.credentials import read_table
from services.files import file_service
import numpy as np

def write_by_file_url(url: str, files: list[str], config: str) -> None:
    month = config['configs'][0]['lists_range'][0]
    google_doc = read_table(url, month)
    filters = list(file_service.find_filters(config).keys())


    for file in files:
        body = file_service.count_days(google_doc, file_service.get_data_from_file(base64.b64decode(file)), file_service.find_filters(config))

        result = np.zeros(shape=(len(body[0]), len(filters)))
        for k in range(len(body[0])):
            for i in range(len(body)):
                result[k][i] = body[i][k]

        google_doc.update('F3:G26', result.tolist()) #нужен фикс
    pass

def get_lists(url): # for interface use
    google_doc = read_table(url)
    worksheets = google_doc[0].worksheets()
    lists = []
    for ws in worksheets:
        lists.append(ws.title)

    return lists

class GoogleSheetService:
    _credentials_file_name = 'creds.json'

    @classmethod
    def get_file_id_by_url(cls, url: str) -> str | None:
        try:
            return url.split('/')[-2]
        except Exception:
            return None


google_sheets_service = GoogleSheetService()
