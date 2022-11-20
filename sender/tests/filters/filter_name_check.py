import unittest

from models import Filter
from services import filter_service


class FilterNameTest(unittest.TestCase):

    def test_can_create_filter(self) -> None:
        self.assertEqual(filter_service.can_create_filter('', self._create_filters_from_name([])), False)
        self.assertEqual(filter_service.can_create_filter('sss', self._create_filters_from_name(['ss', 's'])), True)
        self.assertEqual(filter_service.can_create_filter('s', self._create_filters_from_name(['s', 's', 's'])), False)
        self.assertEqual(filter_service.can_create_filter('s', self._create_filters_from_name(['ss', 'sss', 's'])), False)
        self.assertEqual(filter_service.can_create_filter('s', self._create_filters_from_name(['ss', 'sss'])), True)

    def _create_filters_from_name(self, names: list[str]) -> list[Filter]:
        return list(map(lambda x: Filter(name=x), names))
