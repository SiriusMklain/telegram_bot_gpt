import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("5807785335:AAFzsYSX0YGiXjVEsNLs6CadazJBdE0t8YQ")


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


bot.polling()