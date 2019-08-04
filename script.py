import telebot



import pandas

def get_weather():
    table=pandas.read_html("https://yandex.ru/pogoda/khanty-mansiysk/details#12" , header=0,parse_dates=['Unnamed: 0'])

    answer=[table[0].values[0][0],table[0].values[1][0],table[0].values[2][0],table[0].values[3][0]]
    return answer

token='781229574:AAGC6K39EQ1VNcf2RTOlLpXg_KWoHPAZTIk'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['get'])
def send_weather(message):
    answer=get_weather()
    message_ans='{} \n {} \n {} \n {} \n'.format(answer[0],answer[1],answer[2],answer[3])
    bot.reply_to(message,message_ans)

bot.polling(0)
