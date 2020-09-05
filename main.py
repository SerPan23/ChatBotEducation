import db
import kb
import settings as se
import telebot
import func as f

bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет, меня зовут E-Bot, я направлен помочь тебе в изучении школьной программы.", reply_markup=kb.markupClose)
    chose_direction(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "math":
        chose_topics(call.message)
    elif call.data == "quadratic_equation":
        # f.send_task(call.message)
        m = send_task(call.message)
        bot.register_next_step_handler(m, get_answer_for_task)
    elif call.data == "to_directions":
        chose_direction(call.message)


@bot.message_handler(func=lambda message: True)
def nextQuestion(message):
    if message.text == 'Следующее задание':
        # f.next_task(message)
        next_task()
        m = send_task(message)
        bot.register_next_step_handler(m, get_answer_for_task)
    elif message.text == 'Повторить':
        m = send_task(message)
        bot.register_next_step_handler(m, get_answer_for_task)
    elif message.text == 'К темам':
        chose_topics(message)


def chose_direction(message):
    bot.send_message(message.chat.id,
                     "Выбери предмет:", reply_markup=kb.directListKb)


def chose_topics(message):
    bot.send_message(message.chat.id, 'Выбери задание:', reply_markup=kb.topicsListKb)


def send_task(message):
    return bot.send_message(message.chat.id, text=db.tasks[db.taskId][0], reply_markup=kb.get_akb())


def get_answer_for_task(message):
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


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

