import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
import json
from sender.models.schemas.google_sheets import GoogleSheetsFilterItem


class FileService:

    def format_fio(self, fio):
        return fio.split()[0] + fio.split()[1]

    def convert_to_dict(self,li):
        it = iter(li)
        res_dct = dict(zip(it, it))
        return res_dct

    def get_data_from_file(self, file):
        org_table = pd.read_excel(file, skiprows=6, usecols=range(0, 6), header=None,
                                  names=['Name', 'Nan', 'Vac_type', 'Nan1', 'Work_days', 'Vac_days'])
        org_table.dropna(axis='columns', inplace=True)
        org_table['Name'] = org_table.apply(lambda row: self.format_fio(row['Name']), axis=1)
        return org_table

    def find_doc_range(self, google_doc, config):
        filters = config['filters']
        columns = []
        for fl in filters:
            columns.append(fl['column'])

        columns = sorted(columns)

        data = google_doc.get_values('A:H') #До 6 столбца
        ws_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        first_entry = int(ws_df[ws_df['A'] == '1'].index[0]) + 1 #aaaaaaaa
        last_entry = int(ws_df.shape[0])

        doc_range = f"{columns[0] + str(first_entry)}:{columns[-1] + str(last_entry)}"

        return doc_range

    def find_filters(self, config): # Фильтры указываются явно, как в исходных таблицах
        #config_to_str = json.dumps(config)
        #config_json = json.loads(config_to_str)

        alphabet = {
            'A': 0, 'B': 1, 'C': 2,
            'D': 3, 'E': 4, 'F': 5,
            'G': 6, 'H': 7, 'I': 8,
            'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14,
            'P': 15, 'Q': 16, 'R': 17,
            'S': 18, 'T': 19, 'U': 20,
            'V': 21, 'W': 22, 'X': 23,
            'Y': 24, 'Z': 25
        }
        filters_list = []
        for filtr in config['filters']: #one config
            filters_list.append(list(filtr.values()))

        filters_list = sum(filters_list,[])

        for i in range(len(filters_list)):
            if (len(filters_list[i]) == 1):
                filters_list[i] = alphabet[filters_list[i]]

        filters_dict = self.convert_to_dict(filters_list)


        sorted_filters_list = list(filters_dict.values())

        for i in range(min(sorted_filters_list), max(sorted_filters_list)):
            if i not in sorted_filters_list:
                filters_dict['empty'+str(i)] = i

        sorted_filters = dict(sorted(filters_dict.items(), key=lambda kv: kv[1]))
        return sorted_filters


    def count_days(self, google_doc, org_data, filters_dict):
        data = google_doc.get_values('A:I')       #До 6 столбца !!!!!!!!! Доработать до многих столбцов
        ws_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
        ws_df.drop([0, 1], inplace=True)
        ws_df.drop(columns=['A'], inplace=True)

        filters = list(filters_dict.keys())

        absent_data = {}
        result_values = np.zeros((len(filters), ws_df.shape[0]))  # тк удалены 2 строки



        for filter in filters:
            absent_data[filter] = {}

        for index in org_data.index:
            for i in ws_df.index:
                org_table_name = str(org_data['Name'][index])
                res_table_name = str(ws_df['B'][i] + ws_df['C'][i])
                if fuzz.ratio(org_table_name, res_table_name) > 85:
                    for filter in filters:
                        if (filter in str(org_data['Vac_type'][index])): #Фильтры указываются ЯВНО из исходных таблиц
                            absent_data[filter][i - 1] = str(org_data['Vac_days'][index])

        filters = list(absent_data.keys())
        current_filter = filters[0]

        res_row = 0
        for key, value in absent_data.items():
            if key != current_filter:
                current_filter = key
                res_row += 1
            k = list(value.keys())
            v = list(value.values())

            for i in range(len(k)):
                result_values[res_row][k[i] - 1] = v[i]

        return result_values


file_service = FileService()
