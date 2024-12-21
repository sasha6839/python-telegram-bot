import telebot

token = "7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, ' Start!')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' -- Довжина повідомлення: ' + str(len(message.text)) + ' символів'
    bot.send_message(message.chat.id, mes)


if __name__ == '__main__':
    bot.polling()