import telebot

bot = telebot.TeleBot("5990116004:AAEwFHA8Kc-dA2TpuSsESY-gDbSyJN0kHHA")

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.send_message(message.chat.id, "hi")

    bot.infinity_polling()