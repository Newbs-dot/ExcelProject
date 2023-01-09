from aiogram import executor, types

from bot import dp, BotState
from handlers import end_handler, upload_files_handler, select_lists_handler, table_handler, start_handler
from utils import file_middleware


def init_handlers():
    dp.register_message_handler(start_handler, commands=['start'], state='*')
    dp.register_message_handler(end_handler, commands=['end'], state='*')
    dp.register_message_handler(table_handler, commands=['table'], state='*')
    dp.register_message_handler(upload_files_handler, is_media_group=True, content_types=types.ContentType.DOCUMENT, state=BotState.upload_files)
    dp.register_message_handler(upload_files_handler, content_types=types.ContentType.DOCUMENT, state=BotState.upload_files)
    dp.register_message_handler(select_lists_handler, state=BotState.select_lists)


if __name__ == "__main__":
    init_handlers()
    dp.middleware.setup(file_middleware)
    executor.start_polling(dp, skip_updates=True)
