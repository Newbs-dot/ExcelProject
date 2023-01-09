from settings import settings


class ApiRoute:
    google_sheet: str = f'{settings.API_ROOT_URL}{settings.API_PREFIX}/v1/googleSheets/'


api_route = ApiRoute()
