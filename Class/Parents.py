import Person

class Parent(Person):
    def __init__(self, lastName, firstName, dateOfBirth, address, phoneNumber, age):
        self.lastName = lastName
        self.firstName = firstName
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.age = age
        self.children = []    