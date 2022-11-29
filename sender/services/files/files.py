import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

from services.google_sheets import google_sheets_service


class FileService:

    def format_fio(fio):
        return fio.split()[0] + fio.split()[1]

    def get_data_from_file(self,file):
        org_table = pd.read_excel(file, skiprows=6, usecols=range(0, 6), header=None,
                                  names=['Name', 'Nan', 'Vac_type', 'Nan1', 'Work_days', 'Vac_days'])
        org_table.dropna(axis='columns', inplace=True)
        org_table['Name'] = org_table.apply(lambda row: FileService.format_fio(row['Name']), axis=1) #?????

        return org_table

    def make_body(self,url,worksheet_name,org_data,filters):
        google_doc = google_sheets_service.gspread_read(url,worksheet_name)

        ws_df = pd.DataFrame(google_doc, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        ws_df.drop([0, 1], inplace=True)
        ws_df.drop(columns=['A'], inplace=True)

        absent_data = {}
        result_values = np.zeros((len(filters),30))

        for filter in filters:
            absent_data[filter] = {}

        for index in org_data.index:
            for i in ws_df.index:
                org_table_name = str(org_data['Name'][index])
                res_table_name = str(ws_df['B'][i] + ws_df['C'][i])
                if fuzz.ratio(org_table_name, res_table_name) > 85:
                    for filter in filters:
                        if (filter in str(org_data['Vac_type'][index])):
                            absent_data[filter][i+1] = str(org_data['Vac_days'][index])

        filters = list(absent_data.keys())
        current_filter = filters[0]

        res_row = 0
        for key, value in absent_data.items():
            if key != current_filter:
                current_filter = key
                res_row += 1
            k = list(value.keys())
            v = list(value.values())
            #print(k)
            #print(v)
            for i in range(len(k)):
                result_values[res_row][k[i] - 1] = v[i]

        body = {"valueInputOption": "USER_ENTERED", "data": [{"range": "F3:G22", "majorDimension": "COLUMNS",
                                                             "values": [[result_values[0]], [result_values[1]]]}]}

        return body


file_service = FileService()
