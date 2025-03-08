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

# def send_message(message):
#         bot.send_message(message.chat.id, 'ID : ')
#         bot.register_next_step_handler_by_chat_id(message.chat.id, gh)
#
# def gh(message):
#     thread = threading.Thread(target=send_message_end)
#     thread.start()
#     return message.text
#
# def send_message_end():
#     while True:
#         for i in range(1000):
#             print('norm')
#             bot.send_message(message.text, str(i))
#             time.sleep(int(1))





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


def notification():
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    time3 = ['ss', 1, 2]
    while True:
        for i in range(20):
            cur.execute(f"SELECT notification FROM notes WHERE id='%d'" % i)
            row = cur.fetchone()
            time1 = time.localtime()
            # row[0] = row[0] - len('3')


            if len(str(time1[1])) < 2:
                time3[1] = '0' + str(time1[1])
                time2 = str(time1[0]) + '-' + str(time3[1]) + '-' + str(time3[2]) + ' ' + str(time1[3]) + ':' + str(time1[4])
                print('1' + time2)
                if time2 == row[0]:
                    cur.execute(f"SELECT content FROM notes WHERE id='%d'" % i)
                    row = cur.fetchone()
                    cur.execute(f"SELECT user_id FROM notes WHERE id='%d'" % i)
                    user_id = cur.fetchone()
                    cur.execute(f"SELECT chat_id FROM users WHERE id='%d'" % user_id)
                    chat_id = user_id
                    print(row)
                    bot.send_message(chat_id, row)

            elif len(str(time1[2])) < 2:
                time3[2] = '0' + str(time1[2])
                time2 = str(time1[0]) + '-' + str(time3[1]) + '-' + str(time3[2]) + ' ' + str(time1[3]) + ':' + str(time1[4])
                print('1' + time2)
                print(row[0])
                if time2 == row[0]:
                    cur.execute(f"SELECT content FROM notes WHERE id='%d'" % i)
                    row = cur.fetchone()
                    cur.execute(f"SELECT user_id FROM notes WHERE id='%d'" % i)
                    user_id = cur.fetchone()
                    cur.execute(f"SELECT chat_id FROM users WHERE id='%d'" % user_id)
                    chat_id = user_id
                    print(row)
                    bot.send_message(chat_id, row)



def add_note(message):
    bot.send_message(message.chat.id, "Введіть нотатку: ")
    bot.register_next_step_handler_by_chat_id(message.chat.id, save_note)

def save_note(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()

    if row:
        cur.execute("INSERT INTO notes (user_id, title) VALUES (?, ?)",
                    (row[0], message.text))
        db.commit()

        bot.send_message(message.chat.id, 'Нотатку збережено')

def show_all_notes(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()
    print(row)
    if row:
        cur.execute(f"SELECT id, title, notification FROM notes WHERE deleted=1 AND user_id={row[0]}")
        rows = cur.fetchall()
        print(rows)
        notes = 'Список нотаток:\n\n'
        for r in rows:
            notes += f"/open_{r[0]}) {r[1]}. [{r[2]}]\n"
            print(r)
            print(notes)
            print(rows)
        print(rows)
        bot.send_message(message.chat.id, notes)

def open_note(message, note_id):
    print(f'OPEN_NOTE')
    keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('Нотатку', callback_data='/edit_' + note_id)
    b2 = InlineKeyboardButton('Час', callback_data='/time_' + note_id)
    b3 = InlineKeyboardButton('Видалити', callback_data='/delete_' + note_id)
    keyboard.add(b1, b2)
    keyboard.add(b3)
    print(f'KEYBOARD_ACTION')
    bot.send_message(message.chat.id, f'[{note_id}]Редагувати:', reply_markup=keyboard)


# def edit_step1():
#
#     a = 1
#     return a
#
#
# def edit_step2():
#     edit_note(call, note_id)


def edit_note(call, note_id, a):

    if a:
        a = False
        bot.send_message(call.message.chat.id, "Введіть нову нотатку: ")
        bot.register_next_step_handler_by_chat_id(call.message.chat.id, edit_note, note_id, a)
    else:
        db = sqlite3.connect(c.DB_NAME)
        cur = db.cursor()
        print(note_id)
        cur.execute(f"UPDATE notes SET content='{call.message.text}' WHERE id='%d'" % note_id)
        db.commit()

        if cur.rowcount > 0:
            bot.send_message(call.message.chat.id, 'Нотатка відредагована!')
        else:
            bot.send_message(call.message.chat.id, 'Помилка редагування >:(')

        cur.close()
        db.close()

def time_note(call, note_id, a):

    if a:
        a = False
        bot.send_message(call.message.chat.id, "Введіть час сповіщення: ")
        bot.register_next_step_handler_by_chat_id(call.message.chat.id, time_note, note_id, a)
    else:
        db = sqlite3.connect(c.DB_NAME)
        cur = db.cursor()
        print(note_id)
        cur.execute(f"UPDATE notes SET notification={call.message.text} WHERE id='%d'" % note_id)
        db.commit()

        if cur.rowcount > 0:
            bot.send_message(call.message.chat.id, 'Сповіщення встановлено!')
        else:
            bot.send_message(call.message.chat.id, 'Помилка >:(')

        cur.close()
        db.close()

def delete_note(call, note_id):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("UPDATE notes SET deleted=0 WHERE id=%d" % int(note_id))
    db.commit()

    if cur.rowcount > 0:
        bot.send_message(call.message.chat.id, 'Нотатка видалена!')
    else:
        bot.send_message(call.message.chat.id, 'Помилка видалення >:(')

    cur.close()
    db.close()



# HANDLER
@bot.message_handler(regexp=r"^\/open_\d+$")
def handler_open_id(message):

    values = message.text.split('_')
    print(f'message.text.split : {message.text.split}')
    print(f'values : {values}')
    open_note(message, values[1])

@bot.callback_query_handler(func=lambda call: True)
def handler_note_action(call):
    print(f'call : {call}')
    print(f'call.data.split : {call.data.split}')
    values = call.data.split('_')
    print(f'values : {values}')
    if 2 == len(values):
        if '/delete' == values[0]:
            print(f'DELETE ACTION {values[1]}')
            delete_note(call, values[1])
        elif '/edit' == values[0]:
            a = True
            edit_note(call, values[1], a)
        elif '/time' == values[0]:
            a = True
            time_note(call, values[1], a)



@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'all', 'day', 'end'])
def handler_text_message(message):
    if '/start' == message.text:
        bot_start(message)
    elif '/add' == message.text:
        add_note(message)
    # elif '/edit' == message.text:
    #     pass
    # elif '/del' == message.text:
    #     pass
    elif '/all' == message.text:
        show_all_notes(message)
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass








@bot.message_handler(content_types=['text'])
def message(message):
    bot_start(message)
    # if message.text == '1234':
    #     send_message(message)




    bot_message = message.text
    print(message.chat.id)
    print(message.text)
    bot.send_message(message.chat.id, bot_message)




if __name__ == '__main__':
    thread = threading.Thread(target=notification)
    thread.start()
    bot.infinity_polling()