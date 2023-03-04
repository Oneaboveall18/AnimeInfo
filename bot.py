import telegram.ext
from data import AnimeSearch

TOKEN = "5796713245:AAFuuKH9teGdy72r2LoBeh8FbPAl0RqaBCw"

def start(update, context):
    update.message.reply_text("Hello! Welcome")

def help(update, context):
    update.message.reply_text("Lol")

def handle_message(update, context):
    update.message.reply_text(f"{update.message.text}")

def search(update, context):
    ticker = ""
    ticker += context.args[0]
    ticker += context.args[1]
    anime = AnimeSearch()
    info = anime.anime_search(ticker)
    update.message.reply_text(f"{info}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("search", search))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()