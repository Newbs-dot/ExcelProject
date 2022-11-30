import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Credentials:
    _credentials_file_name = 'creds.json'

    def gspread_read(self, url, month):
        account_credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self._credentials_file_name,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        client = gspread.authorize(account_credentials)
        sheet = client.open_by_url(url)
        ws = sheet.worksheet(month)

        return ws



credentials_service = Credentials()
