from telebot import types
import db


directListKb = types.InlineKeyboardMarkup()  # наша клавиатура
key_math = types.InlineKeyboardButton(text='Математика', callback_data='math')
directListKb.add(key_math)  # добавляем кнопку в клавиатуру


topicsListKb = types.InlineKeyboardMarkup()
key_quadratic_equation = types.InlineKeyboardButton(text='Квадратное уравнение',
                                                            callback_data='quadratic_equation')
topicsListKb.add(key_quadratic_equation)  # добавляем кнопку в клавиатуру


nextBackKb = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Следующее задание')
itembtn2 = types.KeyboardButton("Назад")
nextBackKb.add(itembtn1, itembtn2)

retryKb = types.ReplyKeyboardMarkup(row_width=3)
itembtn12 = types.KeyboardButton('Следующее задание')
itembtn22 = types.KeyboardButton('Повторить')
itembtn32 = types.KeyboardButton("Назад")
retryKb.add(itembtn12, itembtn22, itembtn32)

markupClose = types.ReplyKeyboardRemove(selective=False)

answerKb = types.ReplyKeyboardMarkup(row_width=2)
answbtn1 = types.KeyboardButton(db.tasks[db.taskId][1])
answbtn2 = types.KeyboardButton(db.tasks[db.taskId][2])
answbtn3 = types.KeyboardButton(db.tasks[db.taskId][3])
answerKb.add(answbtn1, answbtn2, answbtn3)