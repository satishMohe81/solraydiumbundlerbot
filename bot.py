import os
from telegram import Update
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update: Update, context):
    update.message.reply_text("🤖 Bot is working!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

print("🚀 Bot started")
updater.start_polling()
updater.idle()
