import gspread
from oauth2client.service_account import ServiceAccountCredentials

from settings import settings


def read_table(url, month=None):
    account_credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        settings.API_GOOGLE_CREDS,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(account_credentials)
    table = client.open_by_url(url)
    # ?
    if month != None:
        ws = table.worksheet(month)
    else:
        ws = table.get_worksheet(0)

    return table, ws  # return table itself and one worksheet selected by month as tuple
