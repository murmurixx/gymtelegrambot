from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Получаем токен из переменной окружения (мы добавим его в Railway позже)
TOKEN = os.getenv("BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой фитнес-бот 💪 Напиши /workout, чтобы получить тренировку!")

# Команда /workout
async def workout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🔥 Тренировка на ягодицы:\n"
        "- Приседания: 3 подхода по 15 повторений\n"
        "- Ягодичный мостик: 3x20\n"
        "- Выпады: 3x12 на каждую ногу"
    )
    await update.message.reply_text(message)

# Настройка и запуск бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("workout", workout))

app.run_polling()
