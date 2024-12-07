import telebot
from telebot import types
import os

token = "7724717353:AAH1itkQBgSDAYcMHS402kXqqE7LLcryJSE"
bot = telebot.TeleBot(token)

list_sticker = ['CAACAgIAAxkBAAO3Z0iqLLOSpaCz8_EVHM7uWxrxLD4AAgUAA8A2TxP5al-agmtNdTYE']


# --- commands ----------------------------------------------------------------
@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, ' Start!')


@bot.message_handler(commands=['stop'])
def bot_stop(message):
    bot.send_message(message.chat.id, 'Stop!')


@bot.message_handler(commands=['key'])
def key_function(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='button 1')
    button_2 = types.KeyboardButton(text='button 2')
    keyboard.add(button_1, button_2)

    msg = bot.send_message(message.chat.id, message.text + 'Key!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, bot_button_function)


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    # print(message.sticker)
    # Отримуємо інформацію про стікер
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji
    bot.reply_to(message, f"Ви надіслали стікер з емоджі {emoji} (ID: {sticker_id})")


@bot.message_handler(commands=['send_sticker'])
def my_send_sticker(message):
    bot.send_sticker(message.chat.id, list_sticker[0])


# --- content_types = text ----------------------------------------------------
@bot.message_handler(content_types=['text'])
def bot_message_text(message):
    if message.text == 'dog':
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        my_file_directory = os.path.join(current_directory, 'sticker', 'dog.webm')

        with open(my_file_directory, "rb") as sticker:
            bot.send_sticker(message.chat.id, sticker)

    else:
        # print(message)
        bot.send_message(message.chat.id, message.text + '... Text work!')


# --- functions ---------------------------------------------------------------
def bot_button_function(message):
    if message.text == 'button 1':
        bot.send_message(message.chat.id, '1')
    elif message.text == 'button 2':
        bot.send_message(message.chat.id, '2')
    else:
        bot.send_message(message.chat.id, 'none')


if __name__ == '__main__':
    bot.infinity_polling()
