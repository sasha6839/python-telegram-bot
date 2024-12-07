import telebot
from telebot import types

token = "7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def send_message(message):
    list_numbers = ['Нуль','Один','Два','Три','Чотири',"П'ять",'Шість']
    request = list_numbers[message.text]



    bot.send_message(message.chat.id, request)


if __name__ == '__main__':
    bot.polling()