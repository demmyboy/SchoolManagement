from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "CBS International Business Program")
        self.root.geometry("1350x800+0+0")
        # creating a frame for the whole project
        mainframe = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="cadet blue")
        mainframe.grid()


# needed to run the application
if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
