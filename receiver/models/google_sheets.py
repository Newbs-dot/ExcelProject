class GoogleSheetsFilterItem:
    name: str
    type: str


class GoogleSheetsUpdateTable:
    url: str
    filters: list[GoogleSheetsFilterItem]
    files: list[bytes]
