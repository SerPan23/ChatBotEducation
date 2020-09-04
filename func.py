import telebot
import kb
import settings as se
import db

bot = telebot.TeleBot(se.TOKEN)


def chose_direction(msg):
    bot.send_message(msg.from_user.id,
                     "Выбери предмет:", reply_markup=kb.directListKb)
