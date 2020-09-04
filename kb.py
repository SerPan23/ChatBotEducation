from telebot import types
import db


directListKb = types.InlineKeyboardMarkup()
key_math = types.InlineKeyboardButton(text='Математика', callback_data='math')
directListKb.add(key_math)


topicsListKb = types.InlineKeyboardMarkup(row_width=1)
key_quadratic_equation = types.InlineKeyboardButton(text='Квадратное уравнение', callback_data='quadratic_equation')
to_directions = types.InlineKeyboardButton(text='К предметам', callback_data='to_directions')
topicsListKb.add(key_quadratic_equation, to_directions)


nextBackKb = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Следующее задание')
itembtn2 = types.KeyboardButton("К темам")
nextBackKb.add(itembtn1, itembtn2)

retryKb = types.ReplyKeyboardMarkup(row_width=3)
itembtn12 = types.KeyboardButton('Следующее задание')
itembtn22 = types.KeyboardButton('Повторить')
itembtn32 = types.KeyboardButton("К темам")
retryKb.add(itembtn12, itembtn22, itembtn32)

markupClose = types.ReplyKeyboardRemove(selective=False)


def get_akb():
    answerKb = types.ReplyKeyboardMarkup(row_width=2)
    answbtn1 = types.KeyboardButton(db.tasks[db.taskId][1])
    answbtn2 = types.KeyboardButton(db.tasks[db.taskId][2])
    answbtn3 = types.KeyboardButton(db.tasks[db.taskId][3])
    answerKb.add(answbtn1, answbtn2, answbtn3)
    return answerKb
