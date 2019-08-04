import telebot
token='781229574:AAGC6K39EQ1VNcf2RTOlLpXg_KWoHPAZTIk'
bot= telebot.TeleBot(token=token)



@bot.message_handler(commands=['start','get'])
def send_answer(message):
    bot.reply_to(message,'Helooo')


bot.polling()
