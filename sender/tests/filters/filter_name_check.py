import unittest

from sender.models import Filter
from services.filters import filter_service


def create_filters_from_name(names: list[str]) -> list[Filter]:
    return list(map(lambda x: Filter(name=x), names))


class FilterNameTest(unittest.TestCase):

    def test_can_create_filter(self) -> None:
        self.assertEqual(filter_service.can_create_filter('', create_filters_from_name([])), False)
        self.assertEqual(filter_service.can_create_filter('sss', create_filters_from_name(['ss', 's'])), True)
        self.assertEqual(filter_service.can_create_filter('s', create_filters_from_name(['s', 's', 's'])), False)
        self.assertEqual(filter_service.can_create_filter('s', create_filters_from_name(['ss', 'sss', 's'])), False)
        self.assertEqual(filter_service.can_create_filter('s', create_filters_from_name(['ss', 'sss'])), True)
