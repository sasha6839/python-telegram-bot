import config
import telebot
import threading
import time
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)
USER_ID = '5930458150'

# SQLITE, DATABASE
db = sqlite3.connect('notebook.db')
cursor = db.cursor()
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
def send_message():
    while True:

        bot_message = "1"
        bot.send_message(USER_ID, bot_message)
        time.sleep(10)


# HANDLER

@bot.message_handler(content_types=['text'])
def message(message):
    bot_message = message.text
    print(message.chat.id)
    bot.send_message(message.chat.id, bot_message)




if __name__ == '__main__':
    thread = threading.Thread(target=send_message)
    thread.start()
    bot.infinity_polling()