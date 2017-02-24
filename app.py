import asyncio
import logging
import soup
import sys
from telegram.ext import CommandHandler, Updater


daily_soup = ''


@asyncio.coroutine
def check_daily_soup(bot, group_chat_id, show_first_soup):
    global daily_soup
    new_soup = soup.get_soup()

    if daily_soup != new_soup:
        daily_soup = new_soup
        if show_first_soup:
            bot.sendMessage(chat_id=group_chat_id,
                            text='Nova sopa no site!\n%s' % daily_soup)
        yield from asyncio.sleep(43200)
    else:
        yield from asyncio.sleep(300)
    asyncio.async(check_daily_soup(bot, group_chat_id), show_first_soup)


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
GROUP_ID = sys.argv[2]
SHOW_FIRST_SOUP = sys.argv[3]

COMMAND_HANDLERS = {'soup': get_today_soup, 'start': start}

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# adding the handlers in order
for key in COMMAND_HANDLERS:
    dispatcher.add_handler(handler=CommandHandler(command=key, callback=COMMAND_HANDLERS[key]))

updater.start_polling()

print('Listening ...')

# starting coroutine
loop = asyncio.get_event_loop()
asyncio.async(check_daily_soup(bot=dispatcher.bot, group_chat_id=GROUP_ID, show_first_soup=(SHOW_FIRST_SOUP == "1")))
loop.run_forever()
