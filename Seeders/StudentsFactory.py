from faker import Faker
from datetime import date
from Class.Student import Student
from Database.connection import db, PyMongoError

fake = Faker()
def insert_studentToDatabase(
    firstName,
    lastName,
    dateOfBirth,
    address,
    phoneNumber,
    age,
    grade,
    className,
    review,
):
    try:
        newStudent = Student(
            firstName,
            lastName,
            dateOfBirth,
            address,
            phoneNumber,
            age,
            grade,
            className,
            review,
            0,
        )

        student = {
            "firstName": newStudent.getFirstName(),
            "lastName": newStudent.getLastName(),
            "dateOfBirth": newStudent.getDateOfBirth(),
            "age": newStudent.getAge(),
            "address": newStudent.getAddress(),
            "phoneNumber": newStudent.getPhoneNumber(),
            "grade": newStudent.getGrade(),
            "className": newStudent.getClassName(),
            "review": newStudent.getReview(),
            "notes": newStudent.getNotes(),
            "avarageRatings": newStudent.getAvarageRatings(),
            "OverallRating": newStudent.getOverallRating(),
        }
        studentsCollection = db["Students"]
        studentsCollection.insert_one(student)
        print("Student added")

    except Exception as e:
        print("Erreur: ", e)

def add_studentFactory():
    if db["Students"].count_documents({}) == 0:
        for i in range(10):
            insert_studentToDatabase(
                db,
                fake.last_name(),
                fake.first_name(),
                date.isoformat(fake.date_of_birth()), # fake.date_of_birth() return a datetime.date object
                fake.address(),
                fake.phone_number(),
                fake.random_int(min=6, max=25),
                fake.random_element(
                    [
                        "CP",
                        "CE1",
                        "CE2",
                        "CM1",
                        "CM2",
                        "6e",
                        "5e",
                        "4e",
                        "3e",
                        "2nde",
                        "1ere",
                        "Tle",
                    ]
                ),
                fake.random_element(
                    [
                        "CP1",
                        "CP2",
                        "CP3",
                        "CE1_A",
                        "CE1_B",
                        "CE1_C",
                        "CE2_A",
                        "CE2_B",
                        "CE2_C",
                        "CM1_A",
                        "CM1_B",
                        "CM1_C",
                        "CM2_A",
                        "CM2_B",
                        "CM2_C",
                        "6e_A",
                        "6e_B",
                        "6e_C",
                        "5e_A",
                        "5e_B",
                        "5e_C",
                        "4e_A",
                        "4e_B",
                        "4e_C",
                        "3e_A",
                        "3e_B",
                        "3e_C",
                        "2nde_A",
                        "2nde_B",
                        "2nde_C",
                        "1ere_A",
                        "1ere_B",
                        "1ere_C",
                        "Tle_A",
                        "Tle_B",
                        "Tle_C",
                    ]
                ),
                fake.text(),
            )
    else:
        print("Students already full")

def add_NoteFactory(first_name, last_name):
    
    try:
        studentsCollection = db["Students"]
        student = studentsCollection.find_one({"lastName": last_name, "firstName": first_name})
    except PyMongoError as e:
        print("Error occurred while fetching student: ", e)
        return False
    
    if student:
        
        subjects=student["notes"].keys() # return the list of subjects
        notes = student["notes"]
        for subject in subjects:
            if not notes[subject]:
                for i in range(10):
                    notes[subject].append(fake.random_int(min=0, max=20))
        try:
            studentsCollection.update_one(
                {"lastName": last_name, "firstName": first_name},
                {"$set": {"notes": notes}},
            )
            print("Note updated")
            return True
        
        except PyMongoError as e:
            print("Error occurred while updating student: ", e)
            return False
    else:
        print("Student " + last_name + " " + first_name + " not found")
        return False
            