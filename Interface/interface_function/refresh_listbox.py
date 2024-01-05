from Interface.common import tk
from Fonctions.StudentsFunction import *

def refresh_listbox(root, db):
    
    listbox = tk.Listbox(root)
    listbox.pack()
    
    listbox.delete(0, tk.END)
    students = getAll_students(db)
    for student in students:
        listbox.insert(tk.END, f"{student['firstName']} {student['lastName']}")