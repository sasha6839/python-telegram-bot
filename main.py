import telebot
from telebot import types

token = '7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE'
bot = telebot.TeleBot(token)
# створюємо об'єкт клавіатури.
# my_buttons = types.ReplyKeyboardMarkup()
# створюємо окрему кнопку.
# btn1 = types.KeyboardButton('Кнопка 1')
# btn2 = types.KeyboardButton('Кнопка 2')
# додаємо кнопки до клавіатури.
# my_buttons.add(btn1, btn2)

# --- BOT MESSAGE ---------------------------------------------------



@bot.message_handler(commands=['start', 'stop', 'b', ''])
def bot_commands(message):
    mes = ''

    if message.text == '/start':
        mes = 'почати'
    elif message.text == '/stop':
        mes = 'зупинити'
    elif message.text == '/b':
        bot_buttons(message)
        return True

    bot.send_message(message.chat.id, mes)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' - !'
    if message.text == 'Саня підор':
        mes = 'Іди нахуй'
    elif message.text == 'Тімур підор':
        mes = 'Звісно'

    bot.send_message(message.chat.id, mes)

def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    btn1 = types.KeyboardButton(text='/start')
    btn2 = types.KeyboardButton(text='/stop')
    btn3 = types.KeyboardButton(text='/b')

    keyboard.add(btn1, btn2, btn3)

    mes = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)

def button_if(message):
    if message.text == '':
        bot.send_message(message.chat.id, 'Кнопка')
    if message.text == '':
        bot.send_message(message.chat.id, 'Кнопка')

if __name__ == '__main__':
    bot.polling()