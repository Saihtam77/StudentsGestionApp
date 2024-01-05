from Database.connection import db, PyMongoError
from Class.Subject import Subject

def addSubject(db, name, coefficient):
    
    try:
        newSubject = Subject(name, coefficient)
    except PyMongoError as e:
        print("Error occurred while fetching subjects: ", e)
        return False
    
    subject={
        "name": newSubject.getName(),
        "coefficient": newSubject.getCoefficient(),
    }
    
    try:
        subjectsCollection = db["Subjects"]
        subjectsCollection.insert_one(subject)
        print("Subject added")
        return True
    except PyMongoError as e:
        print("Error occurred while inserting subject: ", e)
        return False    