import google.auth
import pandas as pd
import gspread


async def check_google_doc_url():
    print('check google doc url')


async def write_data_by_url(url): #data еще
    '''
    if table_data['name'] ==  google_table B[]+C[] (нечеткий поиск)
    if table_data['болезнь'] записываем в google_table F[...]
    else не болезнь записываем в google_table G[...]
    '''
    gc = gspread.oauth(credentials_filename='credentials.json',)

    sh = gc.open("testtable")
    work_sheet = sh.worksheet('январь')

    print(work_sheet.update('F3',123123132))
    print('write data in google doc')
