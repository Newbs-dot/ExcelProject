from settings import settings
from telethon import TelegramClient

api_id = settings.TG_API_ID
api_hash = settings.TG_API_HASH
bot_token = settings.TG_BOT_TOKEN
session_name = settings.TG_SESSION_NAME

bot = TelegramClient(session_name, api_id, api_hash).start(bot_token=settings.TG_BOT_TOKEN)
