import telebot
from telebot import types
from flask import Flask, request
import os

# Получаем токен из переменной окружения
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("❌ Переменная окружения TOKEN не установлена!")

bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # Пример: https://shveibot.onrender.com

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "🧵 <b>Добро пожаловать!</b>\n\n"
        "Мы сотрудничаем с разными швейными производствами, каждое из которых специализируется на определённом виде одежды. "
        "Кто-то шьёт лучшие футболки, кто-то — платья, кто-то — куртки.\n\n"
        "Чтобы вы могли получать только те заказы, которые вам подходят, — мы классифицировали все производства по категориям.\n\n"
        "📌 <b>Перейдите в общую группу с информацией и ссылками на все категории:</b>\n"
        "👉 <a href=\"https://t.me/+ax5rxFt7TN0zYzMy\">Вступить в группу «Виды пошива»</a>\n\n"
        "Если возникнут вопросы — напишите нашему менеджеру 👇"
    )

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📲 Связаться с менеджером", url="https://t.me/PavelMorozovEkat"))

    bot.send_message(
        message.chat.id,
        text,
        parse_mode='HTML',
        reply_markup=markup,
        disable_web_page_preview=True
    )

# Корневой маршрут
@app.route("/", methods=["GET"])
def index():
    return "🤖 ShveiBot is running!"

# Вебхук Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# Устанавливаем webhook при запуске
if __name__ == "__main__":
    if not WEBHOOK_URL:
        raise ValueError("❌ Переменная окружения WEBHOOK_URL не установлена!")

    # Удаляем предыдущий webhook
    bot.remove_webhook()
    
    # Устанавливаем новый webhook
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
