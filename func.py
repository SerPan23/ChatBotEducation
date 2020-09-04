import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)


def chose_direction(message):
    bot.send_message(message.chat.id,
                     "Выбери предмет:", reply_markup=kb.directListKb)


def chose_topics(message):
    bot.send_message(message.chat.id, 'Выбери задание:', reply_markup=kb.topicsListKb)


def send_task(message):
    print(db.taskId)
    return bot.send_message(message.chat.id, text=db.tasks[db.taskId][0], reply_markup=kb.get_akb())


def get_answer_for_task(message):
    print('test')
    if message.text == db.tasks[db.taskId][1]:
        bot.send_message(message.chat.id, text='Правильно',
                         reply_markup=kb.nextBackKb)
    else:
        bot.send_message(message.chat.id, text='Неправильно',
                         reply_markup=kb.retryKb)


def next_task():
    if db.taskId == 0:
        db.taskId += 1
    else:
        db.taskId = 0

