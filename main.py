import telebot

token = '7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def botmessage(message):
    mes = message.text + ' - Це написав класний хлопець!'
    bot.send_message(message.chat.id, mes)

bot.polling()