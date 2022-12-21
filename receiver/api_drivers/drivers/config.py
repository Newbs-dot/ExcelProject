from ..api_route import api_route
from ..request import send_post_request


class ConfigsDriver:
    @classmethod
    async def create_config(cls, telegram_id: str, file: str) -> None:
        await send_post_request(f'{api_route.users}configs', {'telegram_id': telegram_id, 'file': file})

        return


config_driver = ConfigsDriver()
