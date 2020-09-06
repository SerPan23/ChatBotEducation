import pymongo
import settings as se
taskId = 0
tasks = [['3x^2 - 14x - 5 = 0', '5, 1/3', '10, 5/8', '1/9, 0'], ['x^2 - x + 5 = 0', '2', '6', '10']]

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]
lessons = mdb.lessons
tasks = mdb.tasks

def add_lesson(name, show_name):
    lesson = {
        "name": name,
        "show_name": show_name,
        "topics": {}
    }
    lessons.insert_one(lesson).inserted_id


def add_topic(lesson_name, name, show_name):
    item = lessons.find_one({"name": lesson_name})
    topics = item['topics']
    topics.update({name: show_name})
    newitem = {
        "name": item['name'],
        "show_name": item['show_name'],
        "topics": topics
    }
    lessons.replace_one({"name": lesson_name}, newitem)


def del_topic(lesson_name, name):
    item = lessons.find_one({"name": lesson_name})
    topics = item['topics']
    del topics[name]
    newitem = {
        "name": item['name'],
        "show_name": item['show_name'],
        "topics": topics
    }
    lessons.replace_one({"name": lesson_name}, newitem)


def add_task(topic, task, answers, rightId):
    task = {
        "topic": topic,
        "task": task,
        "answers": answers,
        "rightId": rightId
    }
    tasks.insert_one(task).inserted_id


def give_lessons():
    l = []
    for i in lessons.find():
        l.append(i)
    return l


def give_topics(lesson_name):
    item = lessons.find_one({"name": lesson_name})
    topics = item['topics']
    return topics



# add_lesson("math", "Математика")
# add_task("quadratic_equation", "Тестовое задание", ['1', '2', '3', '4'], 1)
# add_topic('math', "test_topic", "Тестовый топик")
# del_topic('math', "test_topic2")
