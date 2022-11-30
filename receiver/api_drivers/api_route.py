from settings import settings


class ApiRoute:
    google_sheet: str = f'{settings.API_ROOT_URL}{settings.API_PREFIX}/v1/googleSheets/'
    users: str = f'{settings.API_ROOT_URL}{settings.API_PREFIX}/v1/users/'
    filters: str = f'{settings.API_ROOT_URL}{settings.API_PREFIX}/v1/filters/'


api_route = ApiRoute()
