import telebot
from telebot import types
import os

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

bot.polling()
