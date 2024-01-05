from Interface.display_main import *

def displayButtons():
    add_button = tk.Button(root, text="Add Student", command=add_student)
    add_button.pack()