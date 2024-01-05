from Interface.common import tk
from Fonctions.StudentsFunction import *

# Show all the students in the listbox
def refresh_listbox(root, db):
    
    listbox = tk.Listbox(root)
    listbox.pack()
    listbox.pack(fill=tk.BOTH, expand=1)  # Make the listbox expand when the window is resized
    
    listbox.delete(0, tk.END)
    students = getAll_students(db)
    for student in students:
        listbox.insert(tk.END, f"{student['firstName']} {student['lastName']}")