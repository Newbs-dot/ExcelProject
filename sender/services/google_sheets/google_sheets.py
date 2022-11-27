import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetService:
    _credentials_file_name = 'creds.json'

    def __int__(self):
        self._service = self._get_auth_service()

    @classmethod
    def _get_auth_service(cls):
        account_credentials = ServiceAccountCredentials.from_json_keyfile_name(
            cls._credentials_file_name,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        http_auth = account_credentials.authorize(httplib2.Http())

        return apiclient.discovery.build('sheets', 'v4', http=http_auth)

    @classmethod
    def get_file_id_by_url(cls, url: str) -> str | None:
        try:
            return url.split('/')[-2]
        except Exception:
            return None

    def read_by_id(self, file_id: str) -> None:
        read_file = self._service.spreadsheets().values().get(
            spreadsheetId=file_id,
            range='A1:E10',
            majorDimension='COLUMNS'
        ).execute()

    def write_by_file_id(self, file_id: str, body: dict[str, str]) -> None:
        write_file = self._service.spreadsheets().values().batchUpdate(
            spreadsheetId=file_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": "B3:C4",
                     "majorDimension": "ROWS",
                     "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
                    {"range": "D5:E6",
                     "majorDimension": "COLUMNS",
                     "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
                ]
            }
        ).execute()


google_sheets_service = GoogleSheetService()
