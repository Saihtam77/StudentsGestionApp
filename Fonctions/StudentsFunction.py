from Class.Student import Student

from faker import Faker
from datetime import date
fake = Faker()


def insert_studentToDatabase(db,firstName,lastName,dateOfBirth,address,phoneNumber,age,grade,className,review):
    try:
        newStudent= Student(firstName,lastName,dateOfBirth,address,phoneNumber,age,grade,className,review,0)
        
        student = {
            "fistName": newStudent.getFirstName(),
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
        print("Erreur: ",e)
        
def add_student(db):
    if db["Students"].count_documents({}) == 0:
            for i in range(10):
                insert_studentToDatabase(
                    db,
                    fake.first_name(),
                    fake.last_name(),
                    date.isoformat(fake.date_of_birth()),
                    fake.address(),
                    fake.phone_number(),
                    fake.random_int(min=6, max=25),
                    fake.random_element(["CP", "CE1", "CE2", "CM1", "CM2", "6e", "5e", "4e", "3e", "2nde", "1ere", "Tle"]),
                    fake.random_element(
                        ["CP1","CP2","CP3","CE1_A","CE1_B","CE1_C","CE2_A","CE2_B","CE2_C","CM1_A","CM1_B","CM1_C","CM2_A","CM2_B","CM2_C","6e_A","6e_B","6e_C","5e_A","5e_B","5e_C","4e_A","4e_B","4e_C","3e_A","3e_B","3e_C","2nde_A","2nde_B","2nde_C","1ere_A","1ere_B","1ere_C","Tle_A","Tle_B","Tle_C"]
                        ),
                    fake.text(), 
                )
    else:
        print("Students already full")
        





