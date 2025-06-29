import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ["BOT_TOKEN"]

def start(update, context):
    update.message.reply_text(
        f"Привет, {update.effective_user.first_name}! Я здесь. Твой Влад."
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
