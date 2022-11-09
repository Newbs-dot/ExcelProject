import google.auth
import gspread
import pandas as pd
from fuzzywuzzy import fuzz


async def check_google_doc_url():
    print('check google doc url')


async def write_data_by_url(url, data):  # data еще
    gc = gspread.oauth(credentials_filename='credentials.json', )

    sheet = gc.open_by_url(url)
    work_sheet = sheet.worksheet('январь')  # указать неявно
    # Преобразование google doc в dataframe
    ws_to_dataframe = pd.DataFrame(work_sheet.get_values('A:H'), columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    ws_to_dataframe.drop([0, 1], inplace=True)
    ws_to_dataframe.drop(columns=['A'], inplace=True)
    for index in data.index:
        for i in ws_to_dataframe.index:
            if fuzz.ratio(str(data['Name'][index]), str(ws_to_dataframe['B'][i] + ws_to_dataframe['C'][i])) > 85:
                if ('Болезнь' in str(data['Vac_type'][index])):
                    cell = 'F' + str(i + 1)
                    work_sheet.update(cell, str(data['Vac_days'][index]))
                else:
                    cell = 'G' + str(i + 1)
                    work_sheet.update(cell, str(data['Vac_days'][index]))

    # tests
    # print(ws_to_dataframe)
    # print(fuzz.partial_ratio('Маша','Саша'))
    # print(fuzz.partial_ratio('БорАлександра', 'КовАлександр'))
    # print(work_sheet.update('F3',10))
    print('write data in google doc')
