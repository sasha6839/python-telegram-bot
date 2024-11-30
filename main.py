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

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Команда СТАРТ!')

@bot.message_handler(commands=['stop'])
def command_start(message):
    bot.send_message(message.chat.id, 'Команда СТОП!')


@bot.message_handler(commands=['open', 'close'])
def commands_open_close(message):
    mes = ''

    if message.text == '/open':
        mes = 'Відкрито'
    elif message.text == '/close':
        mes = 'Закрито'

    bot.send_message(message.chat.id, mes)

@bot.message_handler(commands=['key'])
def key_go(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='Кнопка 1')
    button_2 = types.KeyboardButton(text='Кнопка 2')
    keyboard.add(button_1, button_2)

    bot.send_message(message.chat.id, 'Кнопку натиснуто', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Кнопка 1')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'Ви натиснули кнопку 1.')

@bot.message_handler(func=lambda message: message.text == 'Кнопка 2')
def handle_button_2(message):
    bot.send_message(message.chat.id, 'Ви натиснули кнопку 2.')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji

    bot.reply_to(message, f"Ви надіслали стікер з емодзі {emoji} (ID: {sticker_id})")

@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.text == '1':
        bot.send_sticker(message.shat.id, stickers[0])
        return True

    mes = message.text + ' - !'
    bot.send_message(message.chat.id, mes)



if __name__ == '__main__':
    bot.polling()