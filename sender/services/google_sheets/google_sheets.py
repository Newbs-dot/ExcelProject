import base64
import time

from sender.models import GoogleSheetsFilterItem
from services.credentials import gspread_read
from services.files import file_service


def write_by_file_url(url: str, files: list[str], filters: list[GoogleSheetsFilterItem], month: str) -> None:
    google_doc = gspread_read(url, month)
    cols = file_service.find_filters_cols(google_doc, filters)

    for file in files:
        body = file_service.count_days(google_doc, file_service.get_data_from_file(base64.b64decode(file)), file_service.find_active_filters(filters))
        ranges = file_service.find_doc_range(google_doc)

        i = 0
        for key, val in cols.items():
            for row in range(ranges[0], ranges[1]):
                if (google_doc.cell(row + 1, int(val) + 1).value == '0'):
                    google_doc.update_cell(row + 1, int(val) + 1, body[i][row])
                    time.sleep(0.1)  # лимит на write requests, то же самое для read requests
            i += 1
        pass


class GoogleSheetService:
    _credentials_file_name = 'creds.json'

    @classmethod
    def get_file_id_by_url(cls, url: str) -> str | None:
        try:
            return url.split('/')[-2]
        except Exception:
            return None


google_sheets_service = GoogleSheetService()
