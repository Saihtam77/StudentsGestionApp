from Class.Interface import *
from datetime import datetime


def validate_input_digit(fields,entries):
    for field in fields:
        if not entries[field].get().isdigit():
            messagebox.showerror("Error", "Please enter a number in field :" + field)
            return False
    return True

def validate_input_string(fields,entries):
    for field in fields:
        if not entries[field].get().isalpha():
            messagebox.showerror("Error", "Please enter a text in field: " + field)
            return False
    return True

def validate_input_date(fields,entries):
    for field in fields:
        try:
            datetime.strptime(entries[field].get(), '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Error", "Please enter a date in field: " + field)
            return False
    return True
    