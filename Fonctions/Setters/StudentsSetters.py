from Class.Interface import *
from Class.Student import Student
from Fonctions.validation_input import *

from Database.connection import db,PyMongoError

from Fonctions.Display.StudentsDisplay import refresh_listbox


""" database insertion functions """

    
fields = [
    "firstName",
    "lastName",
    "dateOfBirth",
    "address",
    "phone_number",
    "age",
    "grade",
    "className",
    "review",
]
entries = {}

for field in fields:
    label = tk.Label(root_window.frameRight, text=field)
    label.pack()
    entries[field] = tk.Entry(root_window.frameRight)
    entries[field].pack(padx=10, pady=10)
    

def clean_entries():
        for field in fields:
            entries[field].delete(0, tk.END)
   
def validation_Student():
    if not validate_input_string(["firstName", "lastName"], entries):
        return False
    if not validate_input_date(["dateOfBirth"], entries):
        return False
    if not validate_input_digit(["age", "grade"], entries):
        return False
    if not validate_input_string(["className"], entries):
        return False
    if not validate_input_digit(["phone_number"], entries):
        return False
    if not validate_input_string(["review"], entries):
        return False
    return True


def add_student():
    
    if validation_Student():        
        try:
            newStudent = Student(entries["firstName"].get(), entries["lastName"].get(), entries["dateOfBirth"].get(), entries["address"].get(), entries["phone_number"].get(), entries["age"].get(), entries["grade"].get(), entries["className"].get(), entries["review"].get(), 0)
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
            refresh_listbox()
            clean_entries()
            return True

        except PyMongoError as e:    
            print("Error occurred while adding student: ", e)
            return False 



""" Notes functions """
def calculate_avarageRatings(firstName, lastName, subject):
    try:
        studentsCollection = db["Students"]
        student = studentsCollection.find_one(
            {"lastName": lastName, "firstName": firstName}
        )
    except PyMongoError as e:
        print("Error occurred while fetching student", e)
        return False

    if student:
        notes = student["notes"]
        avarageRatings = student["avarageRatings"]
        sum = 0
        if subject in notes:
            for note in notes[subject]:
                sum += note
                
            avarageRatings[subject] = sum / len(notes[subject])
            print(avarageRatings[subject])
            
            try:
                studentsCollection.update_one(
                    {"lastName": lastName, "firstName": firstName},
                    {"$set": {"avarageRatings": avarageRatings}},
                )
                print("AvarageRatings updated")
                return True
            except PyMongoError as e:
                print("Error occurred while updating student: ", e)
                return False
        else:
            print("Subject" + subject + " not found")
            return False
    else:
        print("Student " + lastName + " " + firstName + " not found")
        return False


def calculate_OverallRating(firstName, lastName):
    # try find the student
    try:
        studentsCollection = db["Students"]
        student = studentsCollection.find_one(
            {"lastName": lastName, "firstName": firstName}
        )
    except  PyMongoError as e:
        print("Error occurred while fetching student", e)
        return False

    # if student exists in the database then update it
    if student:
        avarageRatings = student["avarageRatings"]
        overallRating = student["OverallRating"]
        sum = 0
        
        for subject in avarageRatings:
            sum += avarageRatings[subject]
            overallRating = sum / len(avarageRatings)
        print(overallRating)
        
        # ajoute dans la base de donner
        try:
            studentsCollection.update_one(
                {"lastName": lastName, "firstName": firstName},
                {"$set": {"avarageRatings": avarageRatings, "OverallRating": overallRating}},
            )
            print("OverallRating updated")
            return True
        except PyMongoError as e:
            print("Error occurred while updating student: ", e)
            return False
    else:
        print("Student " + lastName + " " + firstName + " not found")
        return False
        
        
def add_Note(first_name, last_name, subject, note):
    try:
        studentsCollection = db["Students"]

        student = studentsCollection.find_one({"lastName": last_name, "firstName": first_name})
    except PyMongoError as e:
        print("Error occurred while fetching student: ", e)
        return False

    if student:
        notes = student["notes"]
        if subject in notes:
            notes[subject].append(note)
            try:
                studentsCollection.update_one(
                    {"lastName": last_name, "firstName": first_name},
                    {"$set": {"notes": notes}},
                )
                print("Note added")
                calculate_avarageRatings(db, first_name, last_name, subject)
                # calculate_OverallRating(db, first_name, last_name)
                return True
            except PyMongoError as e:
                print("Error occurred while updating student: ", e)
                return False
        else:
            print("Subject not found")
            return False
    else:
        print("Student not found")
        return False
 