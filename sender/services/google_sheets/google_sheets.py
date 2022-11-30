import gspread
from oauth2client.service_account import ServiceAccountCredentials

import services
from services.files import file_service
from services.credentials import credentials_service

from tests.files import tables_in_bytes


class GoogleSheetService:
    _credentials_file_name = 'creds.json'

    @classmethod
    def get_file_id_by_url(cls, url: str) -> str | None:
        try:
            return url.split('/')[-2]
        except Exception:
            return None

    def write_by_file_url(self, url: str,month: str) -> None:
        #res_doc = credentials_service.gspread_read(self.get_file_id_by_url(url),month)
        #res_doc.update('filters_range', [[1, 2], [3, 4]])
        pass

google_sheets_service = GoogleSheetService()
