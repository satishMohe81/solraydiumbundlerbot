import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable verbose logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🔵 Solana Raydium Bundler active!\n\nSend /help for commands")

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TOKEN:
        logger.error("❌ No TELEGRAM_TOKEN in environment!")
        return

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    
    logger.info("🚀 Bot starting...")
    updater.start_polling()
    logger.info("✅ Bot is now live")
    updater.idle()

if __name__ == "__main__":
    main()
