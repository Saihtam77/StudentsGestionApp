from pymongo import MongoClient
from pymongo.errors import PyMongoError


def connection():
    try:
        client = MongoClient()
        print("Connected successfully!!!")
        db_list = client.list_database_names()
        print("Base de donnéer dispo: ",db_list)
        database = client['StudentsGestionAPP']
        return database
    except PyMongoError as e:
        print("Could not connect to MongoDB: %s" % e)
        return False

db = connection()
    
    