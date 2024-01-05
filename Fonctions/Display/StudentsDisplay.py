from Database.connection import db
from Fonctions.Getters.StudentsGetter import *
from commons import *

""" Display fonction """
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=1)  # Make the listbox expand when the window is resized

def listboxStudents():
    
    try:
        students = getAll_students()
        for student in students:
            listbox.insert(tk.END, f"{student['firstName']} {student['lastName']}")        
        return True
    except:
        messagebox.showerror("Error", "Failed to get students")
        return False
    
def refresh_listbox():
        listbox.delete(0, tk.END)
        listboxStudents()


