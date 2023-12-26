from Class.Person import Person

class Parent(Person):
    Students = []
    
    def __init__(self, lastName, firstName, dateOfBirth, address, phoneNumber, age, Students):
        super().__init__(lastName, firstName, dateOfBirth, address, phoneNumber, age)
        
        self.Students = Students 
    