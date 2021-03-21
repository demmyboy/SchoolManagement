from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.ttk import Combobox

import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title("CBS International Business Program")
        self.root.geometry("1500x800+0+0")
        # creating a frame for the whole project
        main_frame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="cadet blue")
        main_frame.grid()

        top_frame1 = Frame(main_frame, bd=5, width=1340, height=50, relief=RIDGE)
        top_frame1.grid(row=2, column=0)

        title_frame = Frame(main_frame, bd=5, width=1340, height=100, relief=RIDGE)
        title_frame.grid(row=0, column=0)

        top_frame2 = Frame(main_frame, bd=5, width=1340, height=450, relief=RIDGE)
        top_frame2.grid(row=1, column=0)

        left_frame = Frame(top_frame2, bd=5, width=1340, height=400, padx=2, relief=RIDGE, bg="cadet blue")
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

        # declare variables
        student_id = StringVar()
        first_name = StringVar()
        last_name = StringVar()
        email = StringVar()
        mobile = StringVar()
        gender = StringVar()

        maths = StringVar()
        science = StringVar()
        add_maths = StringVar()
        spreadsheet = StringVar()
        database = StringVar()
        animation = StringVar()
        digital_graphics = StringVar()
        programming = StringVar()

        # declaring the functions

        def iExit():
            iExit = tkinter.messagebox.askyesno("International Business Program", "Do you want to exit programme")
            if iExit > 0:
                root.destroy()
                return

        def reset():
            student_id.set(" ")
            first_name.set(" ")
            last_name.set(" ")
            email.set(" ")
            mobile.set(" ")
            gender.set(" ")

            maths.set("Core Unit")
            science.set("Core Unit")
            add_maths.set("Core Unit")
            spreadsheet.set("Core Unit")
            database.set("Core Unit")
            animation.set("Core Unit")
            digital_graphics.set("Core Unit")
            programming.set("Core Unit")

        # Creating the widgets -----------------------

        self.lbl_title = Label(title_frame, font=('arial', 56, 'bold'), text="International Business Program ", bd=7)
        self.lbl_title.grid(row=0, column=0, padx=150)

        # creating Entry and Labels

        self.lbl_student_ID = Label(left_frame1, font=('arial', 12, 'bold'), text="Student ID ", bd=7, anchor=W)
        self.lbl_student_ID.grid(row=0, column=0)
        self.txt_student_ID = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=40, justify='left', textvariable=student_id)
        self.txt_student_ID.grid(row=0, column=1)

        self.lbl_first_name = Label(left_frame1, font=('arial', 12, 'bold'), text="First Name ", bd=7, anchor=W)
        self.lbl_first_name.grid(row=1, column=0)
        self.txt_first_name = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=40, justify='left', textvariable=first_name)
        self.txt_first_name.grid(row=1, column=1)

        self.lbl_last_name = Label(left_frame1, font=('arial', 12, 'bold'), text="Last Name", bd=7, anchor=W)
        self.lbl_last_name.grid(row=2, column=0)
        self.txt_last_name = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=40, justify='left', textvariable=last_name)
        self.txt_last_name.grid(row=2, column=1)

        self.lbl_email = Label(left_frame1, font=('arial', 12, 'bold'), text="Email", bd=7, anchor=W)
        self.lbl_email.grid(row=3, column=0)
        self.txt_email = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=40, justify='left', textvariable=email)
        self.txt_email.grid(row=3, column=1)

        self.lbl_mobile = Label(left_frame1, font=('arial', 12, 'bold'), text="Mobile ", bd=7, anchor=W)
        self.lbl_mobile.grid(row=4, column=0)
        self.txt_mobile = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=40, justify='left', textvariable=mobile)
        self.txt_mobile.grid(row=4, column=1)

        self.lbl_gender = Label(left_frame1, font=('arial', 12, 'bold'), text="Gender", bd=7, anchor=W)
        self.lbl_gender.grid(row=5, column=0)
        self.txt_gender = Combobox(left_frame1, font=('arial', 12, 'bold'), state='readonly', width=39, textvariable=gender)
        self.txt_gender.grid(row=5, column=1)
        self.txt_gender['values'] = (' ', 'Female', 'Male')
        self.txt_gender.current(0)

        # subject area ##################

        self.lbl_maths = Label(left_frame2_left, font=('arial', 12, 'bold'), text="Maths", bd=7, anchor='w',
                               justify=LEFT)
        self.lbl_maths.grid(row=0, column=0, sticky=W)
        self.txt_maths = Combobox(left_frame2_left, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=maths)
        self.txt_maths.grid(row=0, column=1)
        self.txt_maths['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_maths.current(0)

        self.lbl_science = Label(left_frame2_left, font=('arial', 12, 'bold'), text="Science", bd=7, anchor='e')
        self.lbl_science.grid(row=1, column=0, sticky=W)
        self.txt_science = Combobox(left_frame2_left, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=science)
        self.txt_science.grid(row=1, column=1)
        self.txt_science['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_science.current(0)

        self.lbl_AddMaths = Label(left_frame2_left, font=('arial', 12, 'bold'), text="AddMaths", bd=7, anchor=W)
        self.lbl_AddMaths.grid(row=2, column=0, sticky=W)
        self.txt_AddMaths = Combobox(left_frame2_left, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=add_maths)
        self.txt_AddMaths.grid(row=2, column=1)
        self.txt_AddMaths['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_AddMaths.current(0)

        self.lbl_spreadsheet = Label(left_frame2_left, font=('arial', 12, 'bold'), text="Spreadsheet", bd=7, anchor=W)
        self.lbl_spreadsheet.grid(row=3, column=0, sticky=W)
        self.txt_spreadsheet = Combobox(left_frame2_left, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=spreadsheet)
        self.txt_spreadsheet.grid(row=3, column=1)
        self.txt_spreadsheet['values'] = ('Core Unit', 'Yes', 'Complete')
        self.txt_spreadsheet.current(0)

        # other side of the frame (right)
        self.lbl_database = Label(left_frame2_right, font=('arial', 12, 'bold'), text="Database", bd=7, anchor='w')
        self.lbl_database.grid(row=0, column=0, sticky=W)
        self.txt_database = Combobox(left_frame2_right, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=database)
        self.txt_database.grid(row=0, column=1)
        self.txt_database['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_database.current(0)

        self.lbl_animation = Label(left_frame2_right, font=('arial', 12, 'bold'), text="Animation", bd=7, anchor='w')
        self.lbl_animation.grid(row=1, column=0, sticky=W)
        self.txt_animation = Combobox(left_frame2_right, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=animation)
        self.txt_animation.grid(row=1, column=1)
        self.txt_animation['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_animation.current(0)

        self.lbl_programming = Label(left_frame2_right, font=('arial', 12, 'bold'), text="Programming", bd=7,
                                     anchor='w')
        self.lbl_programming.grid(row=2, column=0, sticky=W)
        self.txt_programming = Combobox(left_frame2_right, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=programming)
        self.txt_programming.grid(row=2, column=1)
        self.txt_programming['values'] = ('Core Unit', 'Yes', 'No', 'Complete')
        self.txt_programming.current(0)

        self.lbl_digital_graphics = Label(left_frame2_right, font=('arial', 12, 'bold'), text="Spreadsheet", bd=7,
                                          anchor='w')
        self.lbl_digital_graphics.grid(row=3, column=0, sticky=W)
        self.txt_digital_graphics = Combobox(left_frame2_right, font=('arial', 12, 'bold'), state='readonly', width=9, textvariable=digital_graphics)
        self.txt_digital_graphics.grid(row=3, column=1)
        self.txt_digital_graphics['values'] = ('Core Unit', 'Yes', 'Complete')
        self.txt_digital_graphics.current(0)

        # Buttons ############################################

        self.btn_add_new = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8,
                                  text='Add New Data')
        self.btn_add_new.grid(row=0, column=0)

        self.print = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Print')
        self.print.grid(row=0, column=1)

        self.btn_display = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8,
                                  text='Display')
        self.btn_display.grid(row=0, column=2)

        self.btn_update = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Update')
        self.btn_update.grid(row=0, column=3)

        self.btn_delete = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Delete')
        self.btn_delete.grid(row=0, column=4)

        self.btn_search = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Search')
        self.btn_search.grid(row=0, column=5)

        self.btn_reset = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Reset',
                                command=reset)
        self.btn_reset.grid(row=0, column=6)

        self.btn_exit = Button(top_frame1, pady=1, bd=4, font=('arial', 16, 'bold'), padx=24, width=8, text='Exit',
                               command=iExit)
        self.btn_exit.grid(row=0, column=7)

        ## info view
        scroll_y = Scrollbar(right_frame1a, orient=VERTICAL)
        self.student_records = ttk.Treeview(right_frame1a, height=18, columns=(
            "stdid", "First Name", "Last Name", "Email", "Mobile", "Gender", "Maths", "Science", "Programing"),
                                            yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="Student ID")
        self.student_records.heading("First Name", text="First Name")
        self.student_records.heading("Last Name", text="Last Name")
        self.student_records.heading("Email", text="Email")
        self.student_records.heading("Mobile", text="Mobile")
        self.student_records.heading("Gender", text="Gender")
        self.student_records.heading("Maths", text="Maths")
        self.student_records.heading("Science", text="Science")
        self.student_records.heading("Programing", text="Programing")

        self.student_records['show'] = 'headings'

        self.student_records.column("stdid", width=70)
        self.student_records.column("First Name", width=100)
        self.student_records.column("Last Name", width=100)
        self.student_records.column("Email", width=70)
        self.student_records.column("Mobile", width=70)
        self.student_records.column("Gender", width=70)
        self.student_records.column("Maths", width=70)
        self.student_records.column("Science", width=95)
        self.student_records.column("Programing", width=100)

        self.student_records.pack(fill=BOTH, expand=1)


# needed to run the application
if __name__ == '__main__':
    root = Tk()
    # w = 1350
    # h = 800
    # ws = root.winfo_screenwidth()
    # hs = root.winfo_screenwidth()
    #
    # x = (ws / 2) - (w / 2)
    # y= (hs / 2) - (h / 2)
    # root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    application = Student(root)
    root.mainloop()
