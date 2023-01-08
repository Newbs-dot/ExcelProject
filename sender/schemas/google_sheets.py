from pydantic import BaseModel


class GoogleSheets(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class GoogleSheetsList(GoogleSheets):
    name_list: list[str]


class GoogleSheetsUpdateTable(GoogleSheets):
    list_name: str
    files: list[str]
