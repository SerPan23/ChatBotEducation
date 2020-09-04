from telebot import types
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