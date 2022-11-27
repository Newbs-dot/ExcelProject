from models import Filter
from models import filter_type, GoogleSheetsFilterItem


class FilterService:

    @classmethod
    def can_create_filter(cls, filter_name: str, filters: list[Filter]) -> bool:
        return filter_name != '' and not any((filter_name in filter.name and len(filter_name) == len(filter.name)) for filter in filters)

    @classmethod
    def check_filter_type(cls, filters: list[GoogleSheetsFilterItem]):
        return all((filter.type == filter_type.Selected or filter.type == filter_type.NotSelected) for filter in filters)


filter_service = FilterService()
