from commons import *
from Fonctions.Setters.StudentsSetters import *

def addStudent_btn():
    add_button = tk.Button(root, text="Add Student", command=add_student)
    add_button.pack()