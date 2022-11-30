from receiver.models import GoogleSheetsFilterItem
from ..api_route import api_route
from ..request import send_post_request


class GoogleSheetsDriver:

    @classmethod
    async def write_data_in_table(cls, url: str, filters: list[GoogleSheetsFilterItem], files: list[str], month: str) -> None:
        await send_post_request(f'{api_route.google_sheet}updateTable', {'url': url, 'filters': filters, 'files': files, 'month': month})

        return


google_sheet_driver = GoogleSheetsDriver()
