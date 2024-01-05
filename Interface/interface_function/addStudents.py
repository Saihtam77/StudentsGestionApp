from Interface.display_main import *

def addStudent():
    fields = ['firstName', 'lastName', 'dateOfBirth', 'address', 'phone_number', 'age', 'grade', 'className', 'review']
    entries = {}
        
    for field in fields:
        label = tk.Label(root, text=field)
        label.pack()
        entries[field] = tk.Entry(root)
        entries[field].pack()
        
    try:
        new_student = Student(firstName.get(), lastName.get(), dateOfBirth.get(), address.get(), phone_number.get(), age.get(), grade.get(), className.get(), review.get())
        add_student(db, new_student)
        refresh_listbox()
    except PyMongoError as e:
        messagebox.showerror("Error", "Failed to add student: " + str(e))