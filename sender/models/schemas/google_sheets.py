from pydantic import BaseModel


class GoogleSheets(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class GoogleSheetsFilterItem(GoogleSheets):
    name: str
    type: str


class GoogleSheetsUpdateTable(GoogleSheets):
    url: str
    files: list[str]
