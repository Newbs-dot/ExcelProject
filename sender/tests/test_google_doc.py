
from sender.services.google_doc import write_data_by_url
import asyncio
from sender.services.document import get_data_from_file
#email бота: bot-testing@probable-sprite-367510.iam.gserviceaccount.com
import unittest
file = 'D:\Code\PythonExcelBot\Orgs\Org1.xlsx'
#Код из туториала гугла для теста
class MyTestCase(unittest.TestCase):
    def test_doc(self):
        data = asyncio.run(get_data_from_file(file))
        asyncio.run(write_data_by_url('https://docs.google.com/spreadsheets/d/1NdTjc7iLh1YcdVwLbfyFSbh9m_8VTjW8YZlS8lMyOXY/edit#gid=1198610154',data))

if __name__ == '__main__':
    unittest.main()
