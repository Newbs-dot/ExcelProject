from aiogram.dispatcher.filters.state import State, StatesGroup


class BotState(StatesGroup):
    upload_files = State()
    select_filters = State()
    select_month = State()
    add_filter = State()
    bot_menu = State()
    send_google_url = State()
    config_file = State()
