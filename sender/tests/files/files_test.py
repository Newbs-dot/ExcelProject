import asyncio
import unittest

from services.document import get_data_from_file
from tables_in_bytes import files


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = []
        for file in files:
            res.append(asyncio.run(get_data_from_file(file)))
        print()


if __name__ == '__main__':
    unittest.main()
