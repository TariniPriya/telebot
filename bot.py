# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
# Variables
updater = Updater(token='1065262834:AAFG-AWBEQiPacJfivR8y30OkUDGbuBa1bY', use_context=True)
dispatcher = updater.dispatcher
# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sup how are you")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")
def horoscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp2")
# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(date_handler)

sign_handler = CommandHandler('horoscope', horoscope)
dispatcher.add_handler(sign_handler)

updater.start_polling()
print('Bot is working')