import telebot

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.send_message(message.chat.id, "hi")

    bot.infinity_polling()
