import config as c
import telebot
import threading
import time
import sqlite3

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
def send_message(message):

    USER_ID = input('USER_ID = ')
    time_send_message = input('time = ')
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute(f" WHERE ")



    while True:
        for bot_message in range(1000):
            print(f"Send {USER_ID} {message.from_user.username} this {bot_message}")
            bot.send_message(USER_ID, bot_message)
            time.sleep(int(time_send_message))


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



# HANDLER

# @bot.message_handler(commands=['start', 'add', 'edit', 'del', 'all', 'day', 'end'])
# def handler_text_message(message):
#     if '/start' == message.text:
#         bot_start(message)
#     elif '/add' == message.text:
#         pass
#     elif '/edit' == message.text:
#         pass
#     elif '/del' == message.text:
#         pass
#     elif '/all' == message.text:
#         pass
#     elif '/day' == message.text:
#         pass
#     elif '/end' == message.text:
#         pass








@bot.message_handler(content_types=['text'])
def message(message):
    bot_start(message)
    bot_message = message.text
    print(message.chat.id)
    bot.send_message(message.chat.id, bot_message)




if __name__ == '__main__':
    thread = threading.Thread(target=send_message)
    thread.start()
    bot.infinity_polling()