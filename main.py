import db
import kb
import settings as se
import telebot
from telebot import types

bot = telebot.TeleBot(se.TOKEN)


tasks = [['3x^2 - 14x - 5 = 0', '5, 1/3', '10, 5/8', '1/9, 0'], ['x^2 - x + 5 = 0', '2', '6', '10']]



@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_math = types.InlineKeyboardButton(text='Математика', callback_data='math')
    keyboard.add(key_math)  # добавляем кнопку в клавиатуру
    bot.send_message(message.from_user.id,
                     "Привет, меня зовут E-Bot, я направлен помочь тебе в изучении школьной программы.")
    bot.send_message(message.from_user.id,
                     "Выбери предмет:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "math":
        keyboard = types.InlineKeyboardMarkup()
        key_quadratic_equation = types.InlineKeyboardButton(text='Квадратное уравнение',
                                                            callback_data='quadratic_equation')
        keyboard.add(key_quadratic_equation)  # добавляем кнопку в клавиатуру
        bot.send_message(call.message.chat.id, 'Выбери задание:', reply_markup=keyboard)
    elif call.data == "quadratic_equation":
        print(db.taskId)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(tasks[db.taskId][1])
        itembtn2 = types.KeyboardButton(tasks[db.taskId][2])
        itembtn3 = types.KeyboardButton(tasks[db.taskId][3])
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(call.message.chat.id, text=tasks[db.taskId][0], reply_markup=markup)
        bot.register_next_step_handler(call.message, get_answer_for_task)


def get_answer_for_task(message):
    if message.text == tasks[db.taskId][1]:
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
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(tasks[db.taskId][1])
        itembtn2 = types.KeyboardButton(tasks[db.taskId][2])
        itembtn3 = types.KeyboardButton(tasks[db.taskId][3])
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.from_user.id, text=tasks[db.taskId][0],
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_answer_for_task)


bot.polling(none_stop=True, interval=0)
