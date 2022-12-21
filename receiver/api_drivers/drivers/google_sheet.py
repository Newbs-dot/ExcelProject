from ..api_route import api_route
from ..request import send_post_request


class GoogleSheetsDriver:

    @classmethod
    async def write_data_in_table(cls, url: str, files: list[str]) -> None:
        await send_post_request(f'{api_route.google_sheet}updateTable', {'url': url, 'files': files})

        return


google_sheet_driver = GoogleSheetsDriver()
