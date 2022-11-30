import json

from receiver.models import Filter
from ..request import send_get_request, send_post_request
from ..api_route import api_route


class FiltersDriver:
    @classmethod
    async def get_filters(cls) -> list[Filter]:
        response = await send_get_request(f'{api_route.filters}')

        return json.loads(response)

    @classmethod
    async def create_filter(cls, name: str) -> None:
        await send_post_request(f'{api_route.filters}', {'name': name})

        return


filters_driver = FiltersDriver()
