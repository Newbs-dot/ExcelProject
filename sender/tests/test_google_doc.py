
from sender.services.google_doc import write_data_by_url
import asyncio




#email бота: bot-testing@probable-sprite-367510.iam.gserviceaccount.com
import unittest

#Код из туториала гугла для теста
class MyTestCase(unittest.TestCase):
    def test_doc(self):
        asyncio.run(write_data_by_url(1))

if __name__ == '__main__':
    unittest.main()
