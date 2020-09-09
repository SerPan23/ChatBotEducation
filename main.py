import db
import kb
import settings as se
import telebot
from random import randint

bot = telebot.TeleBot(se.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет, меня зовут E-Bot, я направлен помочь тебе в изучении школьной программы.", reply_markup=kb.markupClose)

    photo = open(db.testPhoto, 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, "FILEID")

    chose_direction(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "math":
        db.direct = call.data
        chose_topics(call.message, db.direct)
    elif call.data == "to_directions":
        chose_direction(call.message)
    elif call.data[0:9] == "topicCall":
        db.topic = call.data[10:]
        m = send_task(call.message, db.topic)
        if m != -1:
            # print(m[1])
            db.add_user_taskid(call.message.chat.id, m[1])
            bot.register_next_step_handler(m[0], get_answer_for_task)
    # print(call.data[0:9])


@bot.message_handler(func=lambda message: True)
def nextQuestion(message):
    if message.text == 'Следующее задание':
        m = send_task(message, db.topic)
        db.add_user_taskid(message.chat.id, m[1])
        bot.register_next_step_handler(m[0], get_answer_for_task)
    elif message.text == 'Повторить':
        m = send_task(message, db.topic, db.give_user_taskid(message.chat.id))
        db.add_user_taskid(message.chat.id, m[1])
        bot.register_next_step_handler(m[0], get_answer_for_task)
    elif message.text == 'К темам':
        chose_topics(message, db.direct)


def chose_direction(message):
    bot.send_message(message.chat.id,
                     "Выбери предмет:", reply_markup=kb.directListKb)


def chose_topics(message, lesson):
    bot.send_message(message.chat.id, 'Выбери задание:', reply_markup=kb.get_topics_list(lesson))


def send_task(message, topic, tid=''):
    if(tid != ''):
        t = db.give_tasks_by_id(db.give_user_taskid(message.chat.id))
        return [bot.send_message(message.chat.id, text=t['task'], reply_markup=kb.get_akb(t['answers'])), t['_id']]
    else:
        tasks = db.give_tasks(topic)
        if len(tasks) == 0:
            bot.send_message(message.chat.id, text='Заданий нет', reply_markup=kb.markupClose)
            return -1
        else:
            n = get_task_number(tasks)
            print(n)
            t = tasks[int(n)]
            return [bot.send_message(message.chat.id, text=t['task'], reply_markup=kb.get_akb(t['answers'])), t['_id']]


def get_answer_for_task(message):
    t = db.give_tasks_by_id(db.give_user_taskid(message.chat.id))
    if message.text == t['answers'][t['rightId']]:
        bot.send_message(message.chat.id, text='Правильно',
                         reply_markup=kb.nextBackKb)
    else:
        bot.send_message(message.chat.id, text='Неправильно',
                         reply_markup=kb.retryKb)


def get_task_number(tasks):
    n = randint(0, len(tasks)-1)
    return n


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

