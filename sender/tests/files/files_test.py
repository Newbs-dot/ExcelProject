import unittest

from sender.models.schemas.google_sheets import GoogleSheetsFilterItem

from services.credentials import credentials_service
from services.files import file_service
from tables_in_bytes import byte_files


class MyTestCase(unittest.TestCase):
    def test_something(self):
        filters_list = []
        filter1 = GoogleSheetsFilterItem(type='NotSelected', name='Болезнь')
        filter2 = GoogleSheetsFilterItem(type='Selected', name='Отпуск')
        filters_list.append(filter1)
        filters_list.append(filter2)

        google_doc = credentials_service.gspread_read('https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154'
                                                      , 'январь')

        cols = file_service.find_filters_cols(google_doc, filters_list)
        body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]),
                                       file_service.find_active_filters(filters_list))
        ranges = file_service.find_doc_range(google_doc)

        i = 0
        for key, val in cols.items():
            for row in range(ranges[0], ranges[1]):
                google_doc.update_cell(row + 1, int(val) + 1, body[i][row])
            i += 1


if __name__ == '__main__':
    unittest.main()
