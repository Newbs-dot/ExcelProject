from aiogram import executor, types

from handlers import start_handler, end_handler, upload_files_handler, select_filters_handler, send_google_url_handler
from bot import dp, BotState
from utils import file_middleware


def init_handlers():
    dp.register_message_handler(end_handler, commands=['end'], state='*')
    dp.register_message_handler(start_handler, commands=['start'], state='*')
    dp.register_message_handler(upload_files_handler, is_media_group=True, content_types=types.ContentType.DOCUMENT, state=BotState.upload_files)
    dp.register_message_handler(upload_files_handler, content_types=types.ContentType.DOCUMENT, state=BotState.upload_files)
    dp.register_message_handler(select_filters_handler, state=BotState.select_filters)
    dp.register_message_handler(send_google_url_handler, state=BotState.send_google_url)


if __name__ == "__main__":
    init_handlers()
    dp.middleware.setup(file_middleware)
    executor.start_polling(dp, skip_updates=True)
