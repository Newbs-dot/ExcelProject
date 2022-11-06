from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import settings

bot = Bot(token=settings.TG_BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
