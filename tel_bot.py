import time
from config import TOKEN
from back import show_last, show_all
from telegram.ext import *
from handlers import *


def main():
    while True:
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, set_link))
        dp.add_handler(CommandHandler('check', check))
        dp.add_handler(CommandHandler(['go','stop'], work_flow))
        dp.add_handler(CommandHandler('info', info))
        dp.add_handler(CommandHandler('clear', clear))
        #dp.add_handler(CommandHandler('all', get_all))
        dp.add_error_handler(error)


        updater.start_polling()
        updater.idle()


if __name__=='__main__':
    print('Start')
    main()