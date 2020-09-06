import pymongo
import settings as se
taskId = 0
tasks = [['3x^2 - 14x - 5 = 0', '5, 1/3', '10, 5/8', '1/9, 0'], ['x^2 - x + 5 = 0', '2', '6', '10']]

mdb = pymongo.MongoClient(se.MONGODB_LINK)[se.MONGO_DB]


def add_lesson(name, show_name):
    lesson = {
        "name": name,
        "show_name": show_name,
        "topics": []
    }
    lessons = mdb.lessons
    lessons.insert_one(lesson).inserted_id


def give_lessons():
    l = []
    for i in mdb.lessons.find():
        l.append(i)
    return l



# add_lesson("math2", "Математика2")
# for i in mdb.lessons.find():
#     print(i)
