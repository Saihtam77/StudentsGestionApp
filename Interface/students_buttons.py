from Class.Interface import *
from Fonctions.Setters.StudentsSetters import *

def addStudent_btn():
    add_button = ttk.Button(root_window.frameCenter, text="Add student", command=add_student)
    add_button.pack()