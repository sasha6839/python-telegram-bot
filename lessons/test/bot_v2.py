import telebot
from telebot import types

token = "7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def say_bot(message):
    file = open('list_numbers.txt', mode='a')
    try:
        if int(message.text):
            file.write(message.text+'\n')
    except:
        file.close()
        file = open('list.txt', mode='a')
        file.write(str(message.text)+'\n')

    file.close()
    bot.send_message(message.chat.id, "Ok!")

if __name__ == '__main__':
    bot.polling()