from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text('Bosh sahifa 🏠'), handlers.start))
    dp.add_handler(MessageHandler(Filters.text('🛍 Toplamlar'), handlers.models))
    dp.add_handler(MessageHandler(Filters.text("☎️Contact"), handlers.contact))

    dp.add_handler(CallbackQueryHandler(handlers.one_model, pattern="model:"))
    dp.add_handler(MessageHandler(Filters.text , handlers.handle_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()