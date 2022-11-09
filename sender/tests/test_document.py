import unittest
from sender.services.document import get_data_from_file
import asyncio
file = 'D:\Code\PythonExcelBot\Orgs\Org1.xlsx'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(asyncio.run(get_data_from_file(file)))
if __name__ == '__main__':
    unittest.main()
