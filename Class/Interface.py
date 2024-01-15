import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Class for my main window
class Interface ():
    
    def __init__(self):
        master = tk.Tk()
        self.master = master
        self.master.title("StudentGestoinApp")
        self.master.geometry("800x600")
        # self.master.config(bg=bg_color)
        self.master.resizable(True, True)
        # self.master.iconbitmap("images/icon.ico")
        
        # Create a Frame Container
        self.frameTop = tk.Frame(self.master, bg="red")
        self.frameTop.pack(side=TOP, fill='x')
        
        # Create a Frame Container
        self.frameBottom = tk.Frame(self.master, bg="blue")
        self.frameBottom.pack(side=BOTTOM, fill="x")
        
        # Create a Frame Container
        self.frameLeft = tk.Frame(self.master, bg="green")
        self.frameLeft.pack(side=LEFT, fill='y')
        
        # Create a Frame Container
        self.frameRight = tk.Frame(self.master, bg="yellow")
        self.frameRight.pack(side=RIGHT, fill='y')
        
        # Frame in the center
        self.frameCenter = tk.Frame(self.master, bg="pink")
        self.frameCenter.pack(fill="both", expand=True)

# create an instance of the class
root_window = Interface()      
        
        
    