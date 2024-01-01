from Class.Person import Person


class Student(Person):
    
    """ Constructor """
    def __init__(
        self,
        lastName,
        firstName,
        dateOfBirth,
        address,
        phoneNumber,
        age,
        grade,
        className,
        review,
        OverallRating,
    ):
        super().__init__(lastName, firstName, dateOfBirth, address, phoneNumber, age)
    
        """ attributes """
        self.grade = grade
        self.className = className
        self.review = review
        self.OverallRating = OverallRating

        self.notes = {
            "math": [],
            "english": [],
            "science": [],
            "history": [],  
            "art": [],
            "music": [],
            "pe": [],
        }
        self.avarageRatings = {
            "math": 0,
            "english": 0,
            "science": 0,
            "history": 0,
            "art": 0,
            "music": 0,
            "pe": 0,
        }

    """ Getter """
    def getGrade(self):
        return self.grade

    def getClassName(self):
        return self.className

    def getReview(self):
        return self.review

    def getNotes(self):
        return self.notes

    def getOverallRating(self):
        return self.OverallRating

    def getAvarageRatings(self):
        return self.avarageRatings
    
    """ Setter """

    def setGrade(self, grade):
        self.grade = grade
    
    def setClassName(self, className):
        self.className = className
    
    def setReview(self, review):
        self.review = review
        
    
    
        
        
        
        
    
    
    
        
    
    
