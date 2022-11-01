from handlers import start_command_handler, end_command_handler
from receiver.models import bot


def init_handlers():
    bot.add_event_handler(start_command_handler)
    bot.add_event_handler(end_command_handler)


if __name__ == '__main__':
    bot.start()
    init_handlers()
    print('bot start')
    bot.run_until_disconnected()
