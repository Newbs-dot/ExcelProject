from telethon import events

from receiver.models import bot


@bot.on(events.NewMessage(pattern='/start'))
async def start_command_handler(event):
    await event.respond('start')


@bot.on(events.NewMessage(pattern='/end'))
async def end_command_handler(event):
    await event.respond('end')
