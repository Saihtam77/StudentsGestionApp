class Classes:
    
    """ Constructor for the class Classes """
    def __init__(self, name):
        self.name = name
        self.students = [] # Liste pour stocker les instances de Students
        
    
    """ Getters """
    def getName(self):
        return self.name
    
    def getStudents(self):
        return self.students
           
