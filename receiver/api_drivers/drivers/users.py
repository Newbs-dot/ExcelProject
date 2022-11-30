import json

from receiver.models import User
from ..request import send_get_request, send_post_request
from ..api_route import api_route


class UsersDriver:
    @classmethod
    async def get_user(cls, telegram_id: str) -> User:
        response = await send_get_request(f'{api_route.users}?telegram_id={telegram_id}')

        return json.loads(response)

    @classmethod
    async def create_user(cls, telegram_id: str) -> None:
        await send_post_request(f'{api_route.users}', {'telegram_id': telegram_id})

        return


users_driver = UsersDriver()
