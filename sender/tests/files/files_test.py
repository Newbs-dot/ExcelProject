import unittest

from sender.models.schemas.google_sheets import GoogleSheetsFilterItem

from services.credentials import gspread_read
from services.files import file_service
from tables_in_bytes import byte_files
import json
import time
class MyTestCase(unittest.TestCase):
    def test_something(self):

        js = {
            "url": "https://google.com",
            "configs": [
                {  # config1
                    "filters": [
                        {
                            "filter": "Болезнь",
                            "column": "F"
                        },
                        {
                            "filter": "Отпуск",
                            "column": "G"
                        }
                    ],
                    "lists_range": ["list1", "list54"],
                    "excluded_lists": ["list10", "list3"]
                },
                {  # config2
                    "filters": [
                        {
                            "filter": "Фильтр1",
                            "column": "Столбец фильтра1"
                        },
                        {
                            "filter": "Фильтр2",
                            "column": "Столбец фильтра2"
                        }
                    ],
                    "lists_range": ["list1", "list25"],
                    "excluded_lists": ["list9", "list"]
                }
            ]
        }
        google_doc = gspread_read('https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154'
                                                      , 'январь')
        #body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]),filters_dict)
        cols = filters_dict
        #ranges = file_service.find_doc_range(google_doc)
        filters = list(filters_dict.keys())


        for file in byte_files:
            body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]),filters_dict)
            ranges = file_service.find_doc_range(google_doc)

            i = 0
            for key, val in cols.items():
                for row in range(ranges[0], ranges[1]):
                    if ((google_doc.cell(row + 1, int(val) + 1).value == None) or (
                            google_doc.cell(row + 1, int(val) + 1).value == '0')):
                        google_doc.update_cell(row + 1, int(val) + 1, body[i][row])
                        time.sleep(0.1)  # лимит на write requests, то же самое для read requests
                i += 1
            pass

if __name__ == '__main__':
    unittest.main()
