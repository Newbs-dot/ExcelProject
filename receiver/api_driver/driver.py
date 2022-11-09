import httpx

from settings import settings


class GatewayAPIDriver:
    class Route:
        API_GOOGLE_DOC: str = f'{settings.API_ROOT_URL}{settings.API_PREFIX}/v1/googleDoc'

    @classmethod
    async def write_data_by_url(cls, files: list[bytes], filters: list[str], google_doc_url: str) -> httpx.Response:
        data = {'google_doc_url': google_doc_url, 'filters': filters, 'files': files}
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f'{cls.Route.API_GOOGLE_DOC}/write',
                data=data,
            )

        return resp


api_driver = GatewayAPIDriver()
