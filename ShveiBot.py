import telebot
from telebot import types
import os
from flask import Flask
import threading


TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("❌ Переменная окружения TOKEN не установлена!")


bot = telebot.TeleBot(TOKEN)

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

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    bot.polling(none_stop=True)

bot.polling()
