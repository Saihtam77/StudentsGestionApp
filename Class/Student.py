import Person

class Student(Person):
    grade = ""
    className = ""    
    review = ""
    
    notes = {
        "math": [],
        "english": [],
        "science": [],
        "history": [],
        "art": [],
        "music": [],
        "pe": [],
    }
    avarage = {
        "math": 0,
        "english": 0,
        "science": 0,
        "history": 0,
        "art": 0,
        "music": 0,
        "pe": 0,
    }