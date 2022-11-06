from aiogram.dispatcher.filters.state import State, StatesGroup


class BotState(StatesGroup):
    upload_files = State()
    select_filters = State()
    send_google_url = State()
