import unittest

from services.google_sheets import google_sheets_service


class GoogleSheetsTest(unittest.TestCase):
    def test_get_file_sheets_id(self) -> None:
        self.assertEqual(
            google_sheets_service.get_file_id_by_url('https://docs.google.com/spreadsheets/d/1gOhs0se-fZ5QlJ26u4eiErrA7wqHitAXGBkRIClsky8/edit#gid=0'),
            '1gOhs0se-fZ5QlJ26u4eiErrA7wqHitAXGBkRIClsky8',
            True
        )
        self.assertNotEqual(
            google_sheets_service.get_file_id_by_url('https://docs.google.com/spreadsheets/d/1gOhs0se-fZ5QlJ26u4eiErrA7wqHitAXGBkRIClsky8/edit#gid=0'),
            '1gOhs0se-fZ5QlJ26u4eiErrA7wqHitAXGBkRIClsksssssssssy8',
            True
        )
        self.assertEqual(
            google_sheets_service.get_file_id_by_url('ss'),
            None,
            True
        )
