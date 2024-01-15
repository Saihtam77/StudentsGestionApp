from Class.Interface import *
from Database.connection import db
from Fonctions.Getters.StudentsGetter import *

""" Display fonction """
# listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=20)
# listbox.pack()

# Create a Treeview

treeview = ttk.Treeview(root_window.frameCenter, height=20)
treeview.pack(fill="both", expand=True)

style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 12))


# Define the columns
treeview["columns"]=("one")

# Format the columns
treeview.column("#0", width=270, minwidth=270, stretch=tk.NO)
treeview.column("one", width=150, minwidth=150, stretch=tk.NO)

# Define the headings
treeview.heading("#0",text="Name",anchor=tk.W)
treeview.heading("one", text="Date",anchor=tk.W)
    
  
def studentList():
    try:
        students = getAll_students()
        for student in students:
            treeview.insert("", tk.END, text=f"{student['firstName']} {student['lastName']}", values=(student['dateOfBirth']))
        
        return True
    except:
        messagebox.showerror("Error", "Failed to get students")
        return False
    
def refresh_listbox():
    for item in treeview.get_children():
        treeview.delete(item)
    studentList()

