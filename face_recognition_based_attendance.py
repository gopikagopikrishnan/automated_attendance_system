from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Student(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Face Recognition System")
        self.grid()
        self.canvas_width = 1000
        self.canvas_height = 1000
        self.canvas = Canvas(self, 
                             width=self.canvas_width, 
                             height=self.canvas_height, 
                             bg="white")
        self.canvas.grid()

        img = Image.open(r"C:\Users\Gopika\MEENU\MINIPROJECT CSD481\NSS1.jpeg")
        img = img.rotate(0)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 1000, height = 1000)
        
        bg_img = Label(self, image = self.photoimg)
        bg_img.place(x = 0, y = 0, width = 1000, height = 1000)

        title_lbl = Label(bg_img, text = "Student Management System", font = ("times new roman", 35, "bold"), bg = "white", fg = "black")
        title_lbl.place(x = 0, y = -2, width = 1000, height = 50)

        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x = 20, y = 50, width = 950, height = 600)

        #left label frame
        left_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = 'Student Details', font = ("times new roman", 12, "bold"))
        left_frame.place(x = 10, y = 10, width = 500, height = 570)

        img_left = Image.open(r"C:\Users\Gopika\MEENU\MINIPROJECT CSD481\student_management.jpg")

        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image = self.photoimg_left)
        f_lbl.place(x = 1, y = 0, width = 450, height = 130)

        #current course
        current_course_frame = LabelFrame(left_frame, bd = 2, relief = RIDGE, text = 'Current Course Information', font = ("times new roman", 10, "bold"))
        current_course_frame.place(x = 5, y = 135, width = 490, height = 100)

        #Department
        dep_label = Label(current_course_frame, text = "Department", font = ("times new roman", 8, "bold"))
        dep_label.grid(row = 0, column = 0, padx = 5, sticky = W)

        dep_combo = ttk.Combobox(current_course_frame, font = ("times new roman", 8, "bold"), state = "readonly")
        dep_combo["values"] = ("Select Department", "CSE", "ECE", "CE", "ME", "IC", "EEE")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

        #Course
        course_label = Label(current_course_frame, text = "Course", font = ("times new roman", 8, "bold"))
        course_label.grid(row = 0, column = 2, padx = 5, sticky = W)

        course_combo = ttk.Combobox(current_course_frame, font = ("times new roman", 8, "bold"), state = "readonly")
        course_combo["values"] = ("Select Course", "T1", "T2", "T3", "T4", "L1", "L2")
        course_combo.current(0)
        course_combo.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)

        #Year
        year_label = Label(current_course_frame, text = "Year", font = ("times new roman", 8, "bold"))
        year_label.grid(row = 1, column = 0, padx = 5, sticky = W)

        year_combo = ttk.Combobox(current_course_frame, font = ("times new roman", 8, "bold"), state = "readonly")
        year_combo["values"] = ("Select Year", "2020-24", "2021-25", "2022-26", "2023-27")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = W)

        #Semester
        semester_label = Label(current_course_frame, text = "Semester", font = ("times new roman", 8, "bold"))
        semester_label.grid(row = 1, column = 2, padx = 5, sticky = W)

        semester_combo = ttk.Combobox(current_course_frame, font = ("times new roman", 8, "bold"), state = "readonly")
        semester_combo["values"] = ("Select Semester", "1", "3", "5", "7")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx = 2, pady = 5, sticky = W)

        #Class Student Information
        class_student_frame = LabelFrame(left_frame, bd = 2, relief = RIDGE, text = 'Class Student Information', font = ("times new roman", 10, "bold"))
        class_student_frame.place(x = 5, y = 240, width = 490, height = 300)

        #Student ID
        studentId_label = Label(class_student_frame, text = "StudentID", font = ("times new roman", 8, "bold"))
        studentId_label.grid(row = 0, column = 0, padx = 10, sticky = W)
        studentId_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        studentId_entry.grid(row = 0, column = 1, padx = 5, sticky = W)

        #Student Name
        studentname_label = Label(class_student_frame, text = "Student Name", font = ("times new roman", 8, "bold"))
        studentname_label.grid(row = 0, column = 2, padx = 10, sticky = W)
        studentname_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        studentname_entry.grid(row = 0, column = 3, padx = 5, sticky = W)

        #Class Division
        classdiv_label = Label(class_student_frame, text = "Class Division", font = ("times new roman", 8, "bold"))
        classdiv_label.grid(row = 1, column = 0, padx = 10, sticky = W)
        classdiv_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        classdiv_entry.grid(row = 1, column = 1, padx = 5, sticky = W)

        #Roll Number
        roll_label = Label(class_student_frame, text = "Roll No.", font = ("times new roman", 8, "bold"))
        roll_label.grid(row = 1, column = 2, padx = 10, sticky = W)
        roll_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        roll_entry.grid(row = 1, column = 3, padx = 5, sticky = W)

        #Gender
        gender_label = Label(class_student_frame, text = "Gender", font = ("times new roman", 8, "bold"))
        gender_label.grid(row = 2, column = 0, padx = 10, sticky = W)
        gender_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        gender_entry.grid(row = 2, column = 1, padx = 5, sticky = W)

        #Mail ID
        mail_label = Label(class_student_frame, text = "Mail ID", font = ("times new roman", 8, "bold"))
        mail_label.grid(row = 2, column = 2, padx = 10, sticky = W)
        mail_entry = Entry(class_student_frame, width = 20, font = ("times new roman", 8, "bold"))
        mail_entry.grid(row = 2, column = 3, padx = 5, sticky = W)

        #radio button
        radionbtn1 = ttk.Radiobutton(class_student_frame, text = "Take Photo Sample", value = 'Yes')
        radionbtn1.grid(row = 3, column = 0)

        radionbtn2 = ttk.Radiobutton(class_student_frame, text = "No Photo Sample", value = 'No')
        radionbtn2.grid(row = 3, column = 1)

        #button free
        btn_frame = Frame(class_student_frame, bd = 2, relief = RIDGE, bg = 'white')
        btn_frame.place(x = 0, y = 90, width = 700, height = 150)

        save_btn = Button(btn_frame, text = "Save",  width = 70, font=("times new roman", 8, "bold"), bg = 'Blue', fg = "white")
        save_btn.grid(row = 0, column = 0)

        delete_btn = Button(btn_frame, text = "Delete",  width = 70, font=("times new roman", 8, "bold"), bg = 'Red', fg = "white")
        delete_btn.grid(row = 1, column = 0)

        update_btn = Button(btn_frame, text = "Update",  width = 70, font=("times new roman", 8, "bold"), bg = 'Green', fg = "white")
        update_btn.grid(row = 2, column = 0)

        reset_btn = Button(btn_frame, text = "Reset",  width = 70, font=("times new roman", 8, "bold"), bg = 'Black', fg = "white")
        reset_btn.grid(row = 3, column = 0)

        take_photo_btn = Button(btn_frame, text = "Take Photo Sample",  width = 70, font=("times new roman", 8, "bold"), bg = 'Yellow', fg = "black")
        take_photo_btn.grid(row = 4, column = 0)
        
        update_photo_btn = Button(btn_frame, text = "Update Photo Sample",  width = 70, font=("times new roman", 8, "bold"), bg = 'Teal', fg = "white")
        update_photo_btn.grid(row = 5, column = 0)

        #right label frame
        right_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = 'Student Details', font = ("times new roman", 12, "bold"))
        right_frame.place(x = 520, y = 10, width = 400, height = 570)

        img_right = Image.open(r"C:\Users\Gopika\MEENU\MINIPROJECT CSD481\right_frame.jpg")
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame, image = self.photoimg_right)
        f_lbl.place(x = 1, y = 0, width = 380, height = 130)

        #Search System
        search_frame = LabelFrame(right_frame, bd = 2, relief = RIDGE, text = 'Search System', font = ("times new roman", 10, "bold"))
        search_frame.place(x = 5, y = 240, width = 380, height = 300)

        search_label = Label(search_frame, text = "Search By", font = ("times new roman", 8, "bold"), bg = "darkblue", fg="white")
        search_label.grid(row = 0, column = 0, padx = 2, sticky = W)

        search_combo = ttk.Combobox(search_frame, font = ("times new roman", 8, "bold"), state = "readonly")
        search_combo["values"] = ("Select", "Roll No", "Email ID")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        search_entry = ttk.Entry(search_frame, width = 15, font=("times new roman", 13, "bold"))
        search_entry.grid(row = 0, column = 2, padx = 2, sticky = W)

        search_btn = Button(search_frame, text = "Search",  width = 15, font=("times new roman", 8, "bold"), bg = 'Yellow', fg = "black")
        search_btn.grid(row = 1, column = 0, padx = 2)

        showall_btn = Button(search_frame, text = "Show All",  width = 15, font=("times new roman", 8, "bold"), bg = 'Yellow', fg = "black")
        showall_btn.grid(row = 1, column = 1, padx = 2)

        table_frame = Frame(right_frame, bd = 2, bg = 'white', relief = RIDGE)
        table_frame.place(x = 5, y = 320, width = 400, height = 250)

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column = ("Department", "Course", "Year", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)



def main():
    Student().mainloop()

main()
