import db
import kb
import settings as se
import telebot
from telebot import types

bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Привет, меня зовут E-Bot, я направлен помочь тебе в изучении школьной программы.")
    bot.send_message(message.from_user.id,
                     "Выбери предмет:", reply_markup=kb.directListKb)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "math":
        bot.send_message(call.message.chat.id, 'Выбери задание:', reply_markup=kb.topicsListKb)
    elif call.data == "quadratic_equation":
        bot.send_message(call.message.chat.id, text=db.tasks[db.taskId][0], reply_markup=kb.answerKb)
        bot.register_next_step_handler(call.message, get_answer_for_task)


def get_answer_for_task(message):
    if message.text == db.tasks[db.taskId][1]:
        bot.send_message(message.from_user.id, text='Правильно',
                         reply_markup=kb.nextBackKb)
    else:
        bot.send_message(message.from_user.id, text='Неправильно',
                         reply_markup=kb.retryKb)


@bot.message_handler(func=lambda message: True)
def nextQuestion(message):
    if message.text == 'Следующее задание':
        if db.taskId == 0:
            db.taskId += 1
        else:
            db.taskId = 0
        bot.send_message(message.from_user.id, text=db.tasks[db.taskId][0],
                         reply_markup=kb.answerKb)
        bot.register_next_step_handler(message, get_answer_for_task)
    elif message.text == 'Повторить':
        bot.send_message(message.from_user.id, text=db.tasks[db.taskId][0],
                         reply_markup=kb.answerKb)
        bot.register_next_step_handler(message, get_answer_for_task)


bot.polling(none_stop=True, interval=0)
