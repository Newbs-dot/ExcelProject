import json
from types import SimpleNamespace

from models import SuccessResponse, BadResponse, GoogleSheetLists
from ..api_route import api_route
from ..request import send_post_request, send_get_request


def _get_class_by_str_json(str_json: str):
    return json.loads(str_json, object_hook=lambda d: SimpleNamespace(**d))


class GoogleSheetsDriver:

    @classmethod
    async def get_google_sheet_lists(cls) -> GoogleSheetLists | BadResponse:
        response = await send_get_request(f'{api_route.google_sheet}lists')

        return _get_class_by_str_json(response)

    @classmethod
    async def update_google_sheets_table(cls, list_name: str, files: list[str]) -> SuccessResponse | BadResponse:
        response = await send_post_request(f'{api_route.google_sheet}update', {'list_name': list_name, 'files': files})

        return _get_class_by_str_json(response)


google_sheet_driver = GoogleSheetsDriver()
