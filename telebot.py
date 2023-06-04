import telebot

bot = telebot.TeleBot("bot_token") #token for bot
# def command start
@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.send_message(message.chat.id, "hi")
#run bot
bot.infinity_polling()
