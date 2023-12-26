class Person:
    lastName = ""
    firstName = ""
    dateOfBirth = ""
    address = ""
    phoneNumber = ""
    age = 0
    
    def __init__(self, lastName, firstName, dateOfBirth, address, phoneNumber, age):
        self.lastName = lastName
        self.firstName = firstName
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.age = age
    
    """ Getter """
    def getLastName(self):
        return self.lastName
    def getFirstName(self):
        return self.firstName
    def allName(self):
        return self.firstName + " " + self.lastName
    
    def getAge(self):
        return self.age
    def getDateOfBirth(self):
        return self.dateOfBirth
    
    
    def getAddress(self):
        return self.address
    def getPhoneNumber(self):
        return self.phoneNumber
    
    """ Setter """
    def setLastName(self, lastName):
        self.lastName = lastName
    def setFirstName(self, firstName):
        self.firstName = firstName
    def setAge(self, age):
        self.age = age
    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def setAddress(self, address):
        self.address = address
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    
    
    