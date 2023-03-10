import os
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("TOKEN_GPT")
bot = telebot.TeleBot(os.environ.get("TOKEN_TELEGRAM"))


@bot.message_handler(commands=['start'])
def start_message(message, nav=None):
    bot.send_message(message.chat.id, f"Привет  ✌, тут ты можешь всегда узнать ответы на все интересующие тебе вопросы",
                     reply_markup=nav.profileKeyboard)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_input = message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=2047,
        n=1,
        stop=None,
        temperature=0.5
    )
    bot.send_message(message.chat.id, response["choices"][0]["text"])


bot.polling(none_stop=True)
