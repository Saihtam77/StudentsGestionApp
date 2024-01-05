from Interface.common import *
from Database.connection import connection
from Interface.interface_function.refresh_listbox import refresh_listbox


db = connection()
root = tk.Tk()
root.geometry("300x200")  # Set initial size of the window: 300x200 pixels
root.resizable(True, True)  # Make the window resizable in both directions

def start():
    
    refresh_listbox(root, db) # Display the listbox with all the students
    root.mainloop()