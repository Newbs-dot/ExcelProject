import asyncio
import unittest

from services.document import get_data_from_file
from services.files import file_service
from tables_in_bytes import byte_files


class MyTestCase(unittest.TestCase):
    def test_something(self):
        body = file_service.make_body('https://docs.google.com/spreadsheets/d/1vC2Pt9sQWvU8GEQD6xqcaLbdKsd7YESiqF9PwapZUb0/edit#gid=1198610154',
                                     'январь',
                                     file_service.get_data_from_file(byte_files[0]),
                                     ['Болезнь','Отпуск'])
        print(body)


if __name__ == '__main__':
    unittest.main()
