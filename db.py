import pymongo
import settings as se
taskId = 0
tasks = [['3x^2 - 14x - 5 = 0', '5, 1/3', '10, 5/8', '1/9, 0'], ['x^2 - x + 5 = 0', '2', '6', '10']]


client = pymongo.MongoClient(se.MONGODB_LINK)
db = client.test

