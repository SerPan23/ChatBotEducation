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
    f.chose_direction(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "math":
        f.chose_topics(call.message)
    elif call.data == "quadratic_equation":
        # f.send_task(call.message)
        m = f.send_task(call.message)
        bot.register_next_step_handler(m, f.get_answer_for_task)
    elif call.data == "to_directions":
        f.chose_direction(call.message)


@bot.message_handler(func=lambda message: True)
def nextQuestion(message):
    if message.text == 'Следующее задание':
        # f.next_task(message)
        f.next_task()
        m = f.send_task(message)
        bot.register_next_step_handler(m, f.get_answer_for_task)
    elif message.text == 'Повторить':
        m = f.send_task(message)
        bot.register_next_step_handler(m, f.get_answer_for_task)
    elif message.text == 'К темам':
        f.chose_topics(message)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)

