from robot.api.deco import  keyword
from pymongo import  MongoClient

client = MongoClient('mongodb+srv://ryan_silva:Sccp@cluster0.urngcgc.mongodb.net/markX?appName=Cluster0')

db = client['markX']

@keyword('Remove task from database')
def remove_task_by_name(task_name):
    collection = db['tasks']
    collection.delete_many({'text':task_name})
    print('Removendo a tarefa ' + task_name)