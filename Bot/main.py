from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from connection import API_KEY, PROXY
from handler_func import *

logging.basicConfig(format = '%(name)s - %(lelelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot_chat.log')

def main():
    
    mybot = Updater(API_KEY, request_kwargs = PROXY)

    db = mybot.dispatcher
    db.add_handler(CommandHandler("start", greet_user))
    db.add_handler(CommandHandler("planet", planet_constellation))
    db.add_handler(CommandHandler("planetlist", list_planet))
    db.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

    





    
if __name__ == '__main__':

    main()