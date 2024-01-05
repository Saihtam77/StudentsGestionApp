from Database.connection import db

""" getter functions """
def getInfo_student(lastName, firstName):
    try:
        studentsCollection = db["Students"]
        student = studentsCollection.find_one(
            {"lastName": lastName, "firstName": firstName}
        )
        if student:
            print(student)
        else:
            print("Student not found")
    except Exception as e:
        print("Erreur: ", e)

def getAll_students():
    try:
        studentsCollection = db["Students"]
        students = studentsCollection.find()
        return students
    except Exception as e:
        print("Erreur: ", e)
        return False