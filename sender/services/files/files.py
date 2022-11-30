import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

from sender.models.schemas.google_sheets import GoogleSheetsFilterItem


class FileService:

    def format_fio(self, fio):
        return fio.split()[0] + fio.split()[1]

    def get_data_from_file(self, file):
        org_table = pd.read_excel(file, skiprows=6, usecols=range(0, 6), header=None,
                                  names=['Name', 'Nan', 'Vac_type', 'Nan1', 'Work_days', 'Vac_days'])
        org_table.dropna(axis='columns', inplace=True)
        org_table['Name'] = org_table.apply(lambda row: self.format_fio(row['Name']), axis=1)
        return org_table

    def find_active_filters(self, filters: list[GoogleSheetsFilterItem]):
        active_filters = []
        for filter in filters:
            if filter.type == 'Selected':
                active_filters.append(filter.name)

        return active_filters

    def find_doc_range(self, google_doc):
        data = google_doc.get_values('A:H')
        ws_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        first_entry = int(ws_df[ws_df['A'] == '1'].index[0])
        last_entry = int(ws_df.shape[0])
        doc_range = []
        doc_range.append(first_entry)
        doc_range.append(last_entry)
        return doc_range

    def find_filters_cols(self, google_doc, filters):
        # google_doc = credentials_service.gspread_read(url, worksheet_name)
        data = google_doc.get_values('A:H')
        ws_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

        ws_head = ws_df[:1]
        cells = []
        active_filters = self.find_active_filters(filters)

        for i in ws_head:
            for filter in active_filters:
                if fuzz.partial_ratio(filter, str(ws_head[i][0])) > 40:
                    cells.append(str(ws_head.columns.get_loc(i)))

        # filters_df = pd.DataFrame(cells, active_filters, columns=['Column'])
        filters_dict = dict(zip(active_filters, cells))

        return filters_dict

    def count_days(self, google_doc, org_data, filters):
        # google_doc = credentials_service.gspread_read(url, worksheet_name)
        data = google_doc.get_values('A:H')
        ws_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        ws_df.drop([0, 1], inplace=True)
        ws_df.drop(columns=['A'], inplace=True)

        absent_data = {}
        result_values = np.zeros((len(filters), ws_df.shape[0] + 2))  # тк удалены 2 строки

        for filter in filters:
            absent_data[filter] = {}

        for index in org_data.index:
            for i in ws_df.index:
                org_table_name = str(org_data['Name'][index])
                res_table_name = str(ws_df['B'][i] + ws_df['C'][i])
                if fuzz.ratio(org_table_name, res_table_name) > 85:
                    for filter in filters:
                        if (filter in str(org_data['Vac_type'][index])):
                            absent_data[filter][i + 1] = str(org_data['Vac_days'][index])

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
