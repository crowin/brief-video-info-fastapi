from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Обработчик команды start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot!")

# Обработчик команды help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to begin!")

def setup_telegram_bot():
    # Создаем экземпляр Application с токеном
    application = Application.builder().token("YOUR_TELEGRAM_TOKEN").build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота на прослушивание обновлений
    application.run_polling()

# Запуск функции setup_telegram_bot
if __name__ == '__main__':
    setup_telegram_bot()