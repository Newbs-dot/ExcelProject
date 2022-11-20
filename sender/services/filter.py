from models import Filter


class FilterService:

    def can_create_filter(self, filter_name: str, filters: list[Filter]) -> bool:
        return filter_name != '' and not any((filter_name in filter.name and len(filter_name) == len(filter.name)) for filter in filters)


filter_service = FilterService()
