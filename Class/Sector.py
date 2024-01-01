class Sector:
    def __init__(self, name):
        self.name = name
        self.classes = []   # Liste pour stocker les instances de Classes
        self.subjects = []  # Liste pour stocker les instances de Subject

    def getName(self):
        return self.name

    def getClasses(self):
        return self.classes

    def getSubjects(self):
        return self.subjects

    def addSubject(self, subject):
        self.subjects.append(subject)