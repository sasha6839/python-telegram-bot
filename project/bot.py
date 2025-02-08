import config as c
import telebot
import threading
import time
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(c.BOT_TOKEN)


# SQLITE, DATABASE
#

# cursor.execute('''
#     CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     chat_id INTEGER NOT NULL,
#     username TEXT DEFAULT 'Unknown',
#     email TEXT DEFAULT '',
#     deleted INTEGER DEFAULT 1
#     )''')
# cur.execute(''' INSERT INTO user (name, year, title)
#     VALUES ('Sanya', '2000', 'Учень 14а класу')
#     ;''')


# FUNCTIONS
# def send_message_start(message):
#     try:
#         while True:
#             for bot_message in range(1000):
#                 bot.send_message(message.text, '1')
#                 time.sleep(1)
#                 print('norm')
#     except:
#         print('ID is wrong')

# def send_message():
#     USER_ID = input('USER_ID = ')
#     TIME = input('TIME = ')
#
#
#
#     while True:
#         for i in range(1000):
#             bot.send_message(USER_ID, str(i))
#             time.sleep(int(TIME))

def send_message(message):
        bot.send_message(message.chat.id, 'ID : ')
        bot.register_next_step_handler_by_chat_id(message.chat.id, send_message_end)


def send_message_end(message):

    while True:
        for i in range(1000):
            print('norm')
            bot.send_message(message.text, str(i))
            time.sleep(int(1))





def bot_start(message):
    print(message.chat.id)
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute(f"SELECT chat_id FROM users WHERE chat_id='{message.chat.id}'")
    row = cur.fetchone()

    if not row:
        cur.execute(f"INSERT INTO users (chat_id, username) VALUES ('{message.chat.id}', '{message.from_user.username}')")
        db.commit()
        bot.send_message(message.chat.id, "Користувача додано")
    else:
        bot.send_message(message.chat.id, "Ви вже підписані на цього бота")

# def add_note(message):
#     bot.send_message(message.chat.id, "Введіть нотатку: ")
#     bot.register_next_step_handler_by_chat_id(message.chat.id, save_note)
#
# def save_note(message):
#     db = sqlite3.connect(c.DB_NAME)
#     cur = db.cursor()
#
#     cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
#     row = cur.fetchone()
#
#     if row:
#         cur.execute("INSERT INTO notes (user_id, title) VALUES (?, ?)",
#                     (row[0], message.text))
#         db.commit()
#
#         bot.send_message(message.chat.id, 'Нотатку збережено')
#
# def show_all_notes(message):
#     db = sqlite3.connect(c.DB_NAME)
#     cur = db.cursor()
#     cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
#     row = cur.fetchone()
#
#     if row:
#         cur.execute(f"SELECT id, title, notification FROM notes WHERE user_id={row[0]}")
#         rows = cur.fetchall()
#
#         notes = 'Список нотаток:\n\n'
#         for r in rows:
#             notes += f"/edit_{r[0]}) {r[1]}. [{r[2]}]\n"
#
#         bot.send_message(message.chat.id, notes)
#
# def open_note(message, note_id):
#
#     keyboard = InlineKeyboardMarkup()
#     b1 = InlineKeyboardButton('Нотатку', callback_data='/edit_' + note_id)
#     b2 = InlineKeyboardButton('Час', callback_data='/time_' + note_id)
#     b3 = InlineKeyboardButton('Видалити', callback_data='/delete_' + note_id)
#     keyboard.add(b1, b2)
#     keyboard.add(b3)
#
#     bot.send_message(message.chat.id, 'Редагувати:', reply_markup=keyboard)
#
# def edit_note(message, note_id):
#     pass
#
# def time_note(message, note_id):
#     pass
#
# def delete_note(message, note_id):
#     db = sqlite3.connect(c.DB_NAME)
#     cur = db.cursor()
#     cur.execute("UPDATE notes SET deleted=0 WHERE id=%d" % int(note_id))
#     row = cur.fetchone()



# HANDLER
# @bot.message_handler(regexp=r"^\/open_\d+$")
# def handler_open_id(message):
#
#     values = message.text.split('_')
#     open_note(message, int(values[1]))
#
#
# @bot.message_handler(regexp=r"^\/edit_\d+$")
# def handler_edit_id(message):
#
#     values = message.text.split('_')
#     edit_note(message, int(values[1]))
#
#
# @bot.message_handler(regexp=r"^\/time_\d+$")
# def handler_time_id(message):
#
#     values = message.text.split('_')
#     time_note(message, int(values[1]))
#
#
# @bot.message_handler(regexp=r"^\/delete_\d+$")
# def handler_delete_id(message):
#
#     values = message.text.split('_')
#     delete_note(message, int(values[1]))



@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'all', 'day', 'end'])
def handler_text_message(message):
    if '/start' == message.text:
        bot_start(message)
    # elif '/add' == message.text:
    #     add_note(message)
    # elif '/edit' == message.text:
    #     pass
    # elif '/del' == message.text:
    #     pass
    # elif '/all' == message.text:
    #     show_all_notes(message)
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass








@bot.message_handler(content_types=['text'])
def message(message):
    bot_start(message)
    if message.text == '1234':
        send_message(message)




    bot_message = message.text
    print(message.chat.id)
    print(message.text)
    bot.send_message(message.chat.id, bot_message)




if __name__ == '__main__':
    # thread = threading.Thread(target=send_message)
    # thread.start()
    bot.infinity_polling()