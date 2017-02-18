import logging
import soup
import sys
from telegram.ext import CommandHandler, Updater


def get_today_soup(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='A sopa cadastrada no site neste momento é %s' % soup.get_soup())


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Fala galera da sopa!\n\n'
                         'Não precisa mais ficar olhando o site do green pra ver a sopa, deixa comigo!\n\n'
                         'Se precisarem é só digitar /soup')


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = sys.argv[1]

COMMAND_HANDLERS = {'soup': get_today_soup, 'start': start}

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# adding the handlers in order
for key in COMMAND_HANDLERS:
    dispatcher.add_handler(handler=CommandHandler(command=key, callback=COMMAND_HANDLERS[key]))

updater.start_polling()

print('Listening ...')
