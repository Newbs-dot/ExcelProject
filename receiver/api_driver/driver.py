import httpx

from settings import settings


class GatewayAPIDriver:
    _api_root_url: str = settings.API_ROOT_URL
    _api_key: str = settings.API_SECRET_KEY

    class Route:
        USERS: str = '/users'

    @classmethod
    async def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    async def tg_user_create(cls, name: str, chat_id: int) -> httpx.Response:
        url = await cls._build_url(cls.Route.USERS)
        headers = {'x-api-key': cls._api_key}
        data = {'name': name, 'chat_id': chat_id}

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                headers=headers,
                data=data,
            )

        return resp
