import unittest

from sender.models.schemas.google_sheets import GoogleSheetsFilterItem

from services.credentials import read_table
from services.files import file_service
from tables_in_bytes import byte_files
import numpy as np

import json
import time
class MyTestCase(unittest.TestCase):
    def get_lists(self,url):
        google_doc = read_table(url)
        worksheets = google_doc[0].worksheets()
        lists = []
        for ws in worksheets:
            lists.append(ws.title)

        return lists
    def test_something(self):

        js = {
          "url": "https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154",
          "filters": [
            {
              "filter": "Отпуск",
              "column": "I"
            },
            {
              "filter": "Болезнь",
              "column": "F"
            }
          ]
        }

        table = read_table('https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154', 'list2')
        google_doc = table[1]

        cols = file_service.find_filters(js)

        
        
        body = file_service.count_days(google_doc, file_service.get_data_from_file(byte_files[0]), cols)
        print(cols)
        print(body)

        
        ranges = file_service.find_doc_range(google_doc,js)

        #for fltr in js['configs'][0]['filters']:
        #    print(fltr['column'])


        result = np.zeros(shape = (len(body[0]),len(cols)))

        for k in range(len(body[0])):
            for i in range(len(body)):
                result[k][i] = body[i][k]

        google_doc.update('F3:J30', result.tolist())



if __name__ == '__main__':
    unittest.main()
