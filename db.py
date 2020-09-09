import pymongo
import settings as se

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]
lessons = mdb.lessons
tasks = mdb.tasks
users = mdb.users

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


def add_task(topic, task, answers, rightId, decision_url):
    task = {
        "topic": topic,
        "task": task,
        "answers": answers,
        "rightId": rightId,
        "decision_url": decision_url
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


def give_tasks(topic):
    t = []
    for i in tasks.find({"topic": topic}):
        t.append(i)
    return t


def give_tasks_by_id(id):
    t = tasks.find_one({"_id": id})
    return t


def add_user_taskid(userid, taskid):
    u = users.find_one({"id": userid})
    if u == None:
        user = {
            "id": userid,
            "taskid": taskid,
            "direct": '',
            "topic": ''
        }
        users.insert_one(user).inserted_id
    else:
        user = {
            "id": u['id'],
            "taskid": taskid,
            "direct": u['direct'],
            "topic": u['topic']
        }
        users.replace_one({"id": userid}, user)


def add_user_direct(userid, direct):
    u = users.find_one({"id": userid})
    if u == None:
        user = {
            "id": userid,
            "taskid": '',
            "direct": direct,
            "topic": ''
        }
        users.insert_one(user).inserted_id
    else:
        user = {
            "id": u['id'],
            "taskid": u['taskid'],
            "direct": direct,
            "topic": u['topic']
        }
        users.replace_one({"id": userid}, user)


def add_user_topic(userid, topic):
    u = users.find_one({"id": userid})
    if u == None:
        user = {
            "id": userid,
            "taskid": '',
            "direct": '',
            "topic": topic
        }
        users.insert_one(user).inserted_id
    else:
        user = {
            "id": u['id'],
            "taskid": u['taskid'],
            "direct": u['direct'],
            "topic": topic
        }
        users.replace_one({"id": userid}, user)


def give_user_taskid(userid):
    u = users.find_one({"id": userid})
    return u['taskid']


def give_user_direct(userid):
    u = users.find_one({"id": userid})
    return u['direct']


def give_user_topic(userid):
    u = users.find_one({"id": userid})
    return u['topic']



def send_photo_decision(taskid):
    t = tasks.find_one({"_id": id})
    return  t['decision_url']



# add_lesson("math", "Математика")
# add_task("quadratic_equation", "Тестовое задание", ['4', '24', '24',
#                                                      '13'], 1,
#          'https://yadi.sk/i/QmKRd6sPcLuQ2w')
# add_topic('math', "quadratic_equation", "Тестовый топик")
# del_topic('math', "test_topic2")
