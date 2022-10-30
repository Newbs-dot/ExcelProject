from receiver.models import bot
from handlers import *

if __name__ == '__main__':
    bot.start()
    print('bot start')
    bot.run_until_disconnected()
