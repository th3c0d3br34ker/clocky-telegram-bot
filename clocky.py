from telegram.ext import CommandHandler, Updater

from os import getenv
from dotenv import load_dotenv
import datetime
from .utils import *

load_dotenv()

TOKEN = getenv('TELEGRAMBOT_TOKEN')
print(TOKEN)
updater = Updater(token=TOKEN)


def callback_alarm(bot, job):
    bot.send_message(chat_id=job.context,
                     text=datetime.datetime.now().strftime('%H:%M:%S'))


def callback_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Starting!\n'+greeting)
    job_queue.run_repeating(callback_alarm, 3600,
                            context=update.message.chat_id)


def stop_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Stoped!')
    job_queue.stop()


updater.dispatcher.add_handler(CommandHandler(
    'start', callback_timer, pass_job_queue=True))
updater.dispatcher.add_handler(CommandHandler(
    'stop', stop_timer, pass_job_queue=True))

updater.start_polling()

print("Started!")
