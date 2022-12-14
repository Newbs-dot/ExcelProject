import json
import os


class Settings:
    __slots__ = (
        "API_HOST",
        "API_PORT",
        "API_PROJECT_NAME",
        "API_PREFIX",
        "API_GOOGLE_CREDS",
        "API_CONFIG",
    )

    def __init__(self):
        try:
            settings_file = os.path.join(os.path.dirname(os.path.join(os.path.abspath(__file__))), 'settings.json')
            user_settings = json.load(open(settings_file, encoding='utf-8'))

            for user_setting_key in user_settings:
                setattr(self, user_setting_key, user_settings[user_setting_key])

        except IndexError:
            raise IndexError('Неправильное название файла с настройками')
        except FileNotFoundError:
            raise FileNotFoundError('Не найден файл с настройками')
        except json.JSONDecodeError:
            raise json.JSONDecodeError('Файл настройек должен быть json формата')
        except AttributeError:
            raise AttributeError('Нет нужной настройки настроек')


settings = Settings()
