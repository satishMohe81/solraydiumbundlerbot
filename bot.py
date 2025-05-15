import os
from telegram import Update
from telegram.ext import Updater, CommandHandler

def start(update: Update, context):
    update.message.reply_text("✅ Bot is LIVE!")

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("❌ Missing Telegram Token")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
print("🚀 Starting bot...")
updater.start_polling()
