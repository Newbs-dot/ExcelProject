from settings import settings
from telethon import TelegramClient


def init_bot():
    bot = TelegramClient(
        session=settings.TG_SESSION_NAME,
        api_id=settings.TG_API_ID,
        api_hash=settings.TG_API_HASH,
    )

    return bot.start(bot_token=settings.TG_BOT_TOKEN)


async def send_message():
    print('отправляет сообщение пользователю через бота, нужно вызывать инит бот')
