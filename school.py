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
        main_frame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="cadet blue")
        main_frame.grid()

        top_frame1 = Frame(main_frame, bd=5, width=1340, height=50, relief=RIDGE)
        top_frame1.grid(row=2, column=0)

        title_frame = Frame(main_frame, bd=5, width=1340, height=100, relief=RIDGE)
        title_frame.grid(row=0, column=0)

        top_frame2 = Frame(main_frame, bd=5, width=1340, height=450, relief=RIDGE)
        top_frame2.grid(row=1, column=0)

        left_frame = Frame(top_frame2, bd=5, width=1340, height=400, padx =2, relief=RIDGE, bg="cadet blue")
        left_frame.pack(side=LEFT)

        left_frame1 = Frame(left_frame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
        left_frame1.pack(side=TOP, padx=0, pady=0)

        left_frame2 = Frame(left_frame, bd=5, width=600, height=180, padx=2, relief=RIDGE)
        left_frame2.pack(side=TOP, pady=4)

        left_frame2_left = Frame(left_frame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        left_frame2_left.pack(side=LEFT, pady=4)

        left_frame2_right = Frame(left_frame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        left_frame2_right.pack(side=RIGHT)

        right_frame1 = Frame(top_frame2, bd=5, width=320, height=400, padx=2, bg="cadet blue", relief=RIDGE)
        right_frame1.pack(side=RIGHT)

        right_frame1a = Frame(right_frame1, bd=5, width=310, height=300, padx=2, pady=2, relief=RIDGE)
        right_frame1a.pack(side=TOP)

# needed to run the application
if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
s