import unittest

from sender.models.schemas.google_sheets import GoogleSheetsFilterItem

from services.credentials import gspread_read
from services.files import file_service
from tables_in_bytes import byte_files
import numpy as np
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
                    "lists_range": ["1", "list54"],
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
        month = 'январь'
        google_doc = gspread_read('https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154',month)

        #body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]),filters_dict)
        cols = file_service.find_filters(js)
        #ranges = file_service.find_doc_range(google_doc)
        filters = list(cols.keys())
        #print(js['configs'][0]['lists_range'][0])


        body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]), cols)
        ranges = file_service.find_doc_range(google_doc)
        print(cols)
        result = np.zeros(shape = (len(body[0]),len(filters)))
        for k in range(len(body[0])):
            for i in range(len(body)):
                result[k][i] = body[i][k]

        google_doc.update('F3:G26', result.tolist())

        '''
        a = np.zeros(shape = (len(body[0]),len(filters)))
        print(len(body[0]))
        print('body ', body)
        print('filters ', filters)
        print('ranges ', ranges)

        for k in range(len(body[0])):
            for i in range(len(body)):
                a[k][i] = body[i][k]
                
        print(a)
        '''
        #1
        '''
        i = 0
        for key, val in cols.items():
            for row in range(ranges[0], ranges[1]):
                if ((ws.cell(row + 1, int(val) + 1).value == None) or
                        (ws.cell(row + 1, int(val) + 1).value == '0')):
                    ws.update_cell(row + 1, int(val) + 1, body[i][row])
                    time.sleep(0.1)  # лимит на write requests, то же самое для read requests
            i += 1
        pass
        
        
        
        
        for file in byte_files:
            body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]),cols,month)
            ranges = file_service.find_doc_range(google_doc,month)

            i = 0
            for key, val in cols.items():
                for row in range(ranges[0], ranges[1]):
                    if ((ws.cell(row + 1, int(val) + 1).value == None) or
                            (ws.cell(row + 1, int(val) + 1).value == '0')):
                        ws.update_cell(row + 1, int(val) + 1, body[i][row])
                        time.sleep(0.1)  # лимит на write requests, то же самое для read requests
                i += 1
            pass
            '''

if __name__ == '__main__':
    unittest.main()
