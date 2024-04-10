from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import filedialog
import tkinter as tk

var_dep = None


class Attendance:
    def __init__(self, root, supervise_id, supervise_name):
        self.root = root
        self.supervise_id = supervise_id
        self.supervise_name = supervise_name

        # setting tkinter window size
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title(" Attendance System")

        ## Variables
        self.var_student_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend = StringVar()
        self.var_course = StringVar()

        # Icon
        p1 = PhotoImage(file=r'college_images\iconn.png')
        self.root.iconphoto(False, p1)

        # background
        img3 = Image.open(r"college_images\white.jpg")
        img3 = img3.resize((1910, 990), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1910, height=990)

        top_frame = LabelFrame(bg_img, bd=2, relief=RIDGE, font=("Calibri", 14, "bold"), bg="#FFFFFF")
        top_frame.place(x=0, y=0, width=1908, height=70)

        title_lbl = Label(self.root, relief=FLAT, text=" Attendance Management", font=("Calibri", 25, "bold"),
                          bg="#FFFFFF", fg="Black")
        title_lbl.place(x=20, y=4, width=550, height=60)

        # main frame
        main_frm = LabelFrame(bg_img, relief=RIDGE, bg="white")
        main_frm.place(x=10, y=100, width=1890, height=870)
        # Left Label frame
        left_framee = LabelFrame(main_frm, bd=2, relief=RIDGE, text="Student Attendance Details",
                                 font=("Calibri", 14, "bold"), bg="White")
        left_framee.place(x=10, y=30, width=920, height=800)

        left_small_frame = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_small_frame.place(x=15, y=30, width=880, height=100)

        left_sma_label = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_sma_label.place(x=15, y=120, width=880, height=550)

        # Name
        name_label = Label(left_sma_label, text="Student Name:", font=("Calibri", 14, "bold"), bg="#90EE90")
        name_label.grid(row=0, column=0, padx=15, pady=10)
        name_entry = ttk.Entry(left_sma_label, textvariable=self.var_name, width=20, font=("Calibri", 14, "bold"))
        name_entry.grid(row=0, column=1, pady=10, sticky=W)

        # student id
        stu_lab = Label(left_sma_label, text="Student ID:", font=("Calibri", 14, "bold"), bg="#90EE90")
        stu_lab.grid(row=0, column=2, padx=15)
        stu_entry = ttk.Entry(left_sma_label, textvariable=self.var_student_id, width=20, font=("Calibri", 14, "bold"))
        stu_entry.grid(row=0, column=3, pady=20, sticky=W)

        # lec no
        self.lec1 = Label(left_sma_label, text="Lecture 1:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec1.grid(row=2, column=0, pady=15)
        self.lec1_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec1_combo["values"] = ("Yes", "No")
        self.lec1_combo.grid(row=2, column=1, pady=15)
        # lec no
        self.lec2 = Label(left_sma_label, text="Lecture 2:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec2.grid(row=2, column=2, pady=15)
        self.lec2_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec2_combo["values"] = ("Yes", "No")
        self.lec2_combo.grid(row=2, column=3, pady=15)
        # lec no
        self.lec3 = Label(left_sma_label, text="Lecture 3:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec3.grid(row=3, column=0, pady=15)
        self.lec3_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec3_combo["values"] = ("Yes", "No")
        self.lec3_combo.grid(row=3, column=1, pady=15)
        # lec no
        self.lec4 = Label(left_sma_label, text="Lecture 4:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec4.grid(row=3, column=2, pady=15)
        self.lec4_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec4_combo["values"] = ("Yes", "No")
        self.lec4_combo.grid(row=3, column=3, pady=15)
        # lec no
        self.lec5 = Label(left_sma_label, text="Lecture 5:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec5.grid(row=4, column=0, pady=15)
        self.lec5_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec5_combo["values"] = ("Yes", "No")
        self.lec5_combo.grid(row=4, column=1, pady=15)
        # lec no
        self.lec6 = Label(left_sma_label, text="Lecture 6:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec6.grid(row=4, column=2, pady=15)
        self.lec6_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec6_combo["values"] = ("Yes", "No")
        self.lec6_combo.grid(row=4, column=3, pady=15)
        # lec no
        self.lec7 = Label(left_sma_label, text="Lecture 7:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec7.grid(row=5, column=0, pady=15)
        self.lec7_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec7_combo["values"] = ("Yes", "No")
        self.lec7_combo.grid(row=5, column=1, pady=15)
        # lec no
        self.lec8 = Label(left_sma_label, text="Lecture 8:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec8.grid(row=5, column=2, pady=15)
        self.lec8_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec8_combo["values"] = ("Yes", "No")
        self.lec8_combo.grid(row=5, column=3, pady=15)
        # lec no
        self.lec9 = Label(left_sma_label, text="Lecture 9:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec9.grid(row=6, column=0, pady=15)
        self.lec9_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec9_combo["values"] = ("Yes", "No")
        self.lec9_combo.grid(row=6, column=1, pady=15)
        # lec no
        self.lec10 = Label(left_sma_label, text="Lecture 10:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec10.grid(row=6, column=2, pady=15)
        self.lec10_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec10_combo["values"] = ("Yes", "No")
        self.lec10_combo.grid(row=6, column=3, pady=15)
        # lec no
        self.lec11 = Label(left_sma_label, text="Lecture 11:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec11.grid(row=7, column=0, pady=15)
        self.lec11_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec11_combo["values"] = ("Yes", "No")
        self.lec11_combo.grid(row=7, column=1, pady=15)
        # lec no
        self.lec12 = Label(left_sma_label, text="Lecture 12:", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.lec12.grid(row=7, column=2, pady=15)
        self.lec12_combo = ttk.Combobox(left_sma_label, font=("Calibri", 12, "normal"), state="readonly")
        self.lec12_combo["values"] = ("Yes", "No")
        self.lec12_combo.grid(row=7, column=3, pady=15)

        # Course
        ### لو متحددش no , لو خدت منها yes 
        ## عايز update اسم الجدول هوا ال select من الكومبو و السليكتات من 1 - 12 لو يس حط 
## check 
       ## لو ملاقيش database يعمل self destroy و يقول انو معندوش data 
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()

            # Retrieve the data from the database
            cursor.execute(f"SELECT coursid FROM lecturer WHERE lecturer_id = {self.supervise_id};")
            courses = cursor.fetchall()

            # Create a list of course ids
            course_ids = [course[0] for course in courses]

            course_names = []

            for course_id in course_ids:
                cursor.execute(f"SELECT code FROM cours WHERE coursid = {course_id};")
                course_data = cursor.fetchall()
                course_names.extend([course[0] for course in course_data])

            var_dep = tk.StringVar()

            # Create and grid the ttk.Combobox widget
            course_label = ttk.Label(left_small_frame, text="Course", font=("Calibri", 14, "bold"),
                                     background="#90EE90")
            course_label.grid(row=0, column=0, padx=15)

            self.cour_combo = ttk.Combobox(left_small_frame, textvariable=var_dep, font=("Calibri", 12, "normal"),
                                           state="readonly")
            self.cour_combo["values"] = tuple(course_names)
            self.cour_combo.current(0)
            self.cour_combo.grid(row=0, column=1, padx=12, pady=25, sticky="w")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        self.cour_combo.bind("<<ComboboxSelected>>", self.fill_table)

        # course_label = Label(left_small_frame, text="Course", font=("Calibri", 14, "bold"), bg="#90EE90")
        # course_label.grid(row=0, column=2, padx=5)
        # cour_combo = ttk.Combobox(left_small_frame, textvariable=self.var_dep, font=("Calibri", 12, "normal"),
        #                           state="readonly")
        # cour_combo["values"] = ("Select Course", "CSE 510", "CSE 500", "CSE 555", "CSE 302", "CSE 301")
        # cour_combo.current(0)
        # cour_combo.grid(row=0, column=3, padx=12, pady=25, sticky=W)

        # buttons frame
        btn_frame = Frame(left_sma_label, bd=2, relief=FLAT, bg="white")
        btn_frame.place(x=30, y=460, width=830, height=47)



        export_csv = Button(btn_frame, text="Export CSV", command=self.export_to_csv, width=17,
                            font=("Calibri", 13, "bold"), bg="#235e51", fg="white")
        export_csv.grid(row=0, column=3, padx=15)

        update_buttn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("Calibri", 13, "bold"), bg="#235e51",
                              fg="white")
        update_buttn.grid(row=0, column=0)

        reset_btn = Button(btn_frame, text="Reset", textvariable=self.reset, width=17, font=("Calibri", 13, "bold"),
                           bg="#235e51", fg="white")
        reset_btn.grid(row=0, column=2, padx=15)

        # Right Label frame
        right_framee = LabelFrame(main_frm, bd=2, relief=RIDGE, text="Attendance Details", font=("Calibri", 14, "bold"),
                                  bg="white")
        right_framee.place(x=950, y=30, width=915, height=800)
        table_frm = Frame(right_framee, bd=2, relief=RIDGE, bg="white")
        table_frm.place(x=15, y=30, width=880, height=700)

        #### scroll bar for the right frame
        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)
        self.AttendReportTable = ttk.Treeview(table_frm, column=(
        "name", "id", "lec1", "lec2", "lec3", "lec4", "lec5", "lec6", "lec7", "lec8", "lec9", "lec10", "lec11",
        "lec12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=24)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendReportTable.xview)
        scroll_y.config(command=self.AttendReportTable.yview)

        self.AttendReportTable.heading("name", text="Student Name")
        self.AttendReportTable.heading("id", text="Student ID")
        self.AttendReportTable.heading("lec1", text="Lecture 1")
        self.AttendReportTable.heading("lec2", text="Lecture 2")
        self.AttendReportTable.heading("lec3", text="Lecture 3")
        self.AttendReportTable.heading("lec4", text="Lecture 4")
        self.AttendReportTable.heading("lec5", text="Lecture 5")
        self.AttendReportTable.heading("lec6", text="Lecture 6")
        self.AttendReportTable.heading("lec7", text="Lecture 7")
        self.AttendReportTable.heading("lec8", text="Lecture 8")
        self.AttendReportTable.heading("lec9", text="Lecture 9")
        self.AttendReportTable.heading("lec10", text="Lecture 10")
        self.AttendReportTable.heading("lec11", text="Lecture 11")
        self.AttendReportTable.heading("lec12", text="Lecture 12")

        self.AttendReportTable["show"] = "headings"

        self.AttendReportTable.column("id", width=100, anchor=CENTER)
        self.AttendReportTable.column("name", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec1", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec2", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec3", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec4", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec5", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec6", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec7", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec8", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec9", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec10", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec11", width=120, anchor=CENTER)
        self.AttendReportTable.column("lec12", width=120, anchor=CENTER)

        self.AttendReportTable.pack(fill=BOTH, expand=1)


        self.AttendReportTable.bind("<ButtonRelease>", self.get_cursor)




        # Fetch Data

    def update_data(self):

        try:
            update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if update:
                # Connect to the database
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="T12a34G56",
                    database="face_recognizers"
                )
                cursor = connection.cursor()

                # Update the lecture values in the table
                lecture_values = [
                    self.lec1_combo.get(),
                    self.lec2_combo.get(),
                    self.lec3_combo.get(),
                    self.lec4_combo.get(),
                    self.lec5_combo.get(),
                    self.lec6_combo.get(),
                    self.lec7_combo.get(),
                    self.lec8_combo.get(),
                    self.lec9_combo.get(),
                    self.lec10_combo.get(),
                    self.lec11_combo.get(),
                    self.lec12_combo.get()
                ]

                # Update the lecture columns in the table
                for i in range(12):
                    lecture_column = f"lectur{i+1}"
                    lecture_value = 1 if lecture_values[i] == "Yes" else 0
                    query = f"UPDATE {self.cour_combo.get()} SET {lecture_column} = {lecture_value} WHERE studentid = {self.var_student_id.get()}"
                    print(self.cour_combo)
                    print(lecture_column)
                    print(query)
                    cursor.execute(query)

                connection.commit()

                # Display a success message
                messagebox.showinfo("Success", "Student details successfully updated.", parent=self.root)
                
                connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.cour_combo.get()}"
            cursor.execute(query)
            result = cursor.fetchall()
            self.AttendReportTable.delete(*self.AttendReportTable.get_children())
            for row in result:
                student_id = row[0]
                student_name = row[1]
                self.AttendReportTable.insert("", "end", values=(student_id, student_name,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
                
            else:
                # If update is not confirmed
                return

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def fetch_data(self, rows):
        self.AttendReportTable.delete(*self.AttendReportTable.get_children())
        for i in rows:
            self.AttendReportTable.insert("", END, values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
        # export csv

    def export_to_csv(self):
        # Get all the data from the table
        if self.cour_combo.get():
            
            data = []
            for row in self.AttendReportTable.get_children():
                values = [self.AttendReportTable.item(row)['values'][0], self.AttendReportTable.item(row)['values'][1]]
                for i in range(2, 14):
                    values.append(self.AttendReportTable.item(row)['values'][i])
                data.append(values)

            # Define the CSV file path
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            
            if fln:
                if not fln.lower().endswith('.csv'):
                    fln += '.csv'
                # Write the data to the CSV file
                with open(fln, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Student Name", "Student ID", "Lecture 1", "Lecture 2", "Lecture 3", "Lecture 4", "Lecture 5", "Lecture 6", "Lecture 7", "Lecture 8", "Lecture 9", "Lecture 10", "Lecture 11", "Lecture 12"])
                    writer.writerows(data)

        else: 
            messagebox.showerror("Warning","No Lecture Found To Export")
        

        

    def get_cursor(self, event=""):
        cursor_row = self.AttendReportTable.focus()
        content = self.AttendReportTable.item(cursor_row)
        row = content["values"]
        self.var_student_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_dep.set(row[2]),
        self.var_time.set(row[3]),
        self.var_date.set(row[4]),
        self.var_attend.set(row[5])

    def reset(self):
        self.var_student_id.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attend.set("")


    



    def fill_table(self,event):
        global var_dep
        cours = self.cour_combo.get()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()
            query = f"SELECT * FROM {cours}"
            cursor.execute(query)
            result = cursor.fetchall()
            self.AttendReportTable.delete(*self.AttendReportTable.get_children())
            for row in result:
                student_id = row[0]
                student_name = row[1]
                self.AttendReportTable.insert("", "end", values=(student_id, student_name,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))

        except mysql.connector.Error as error:
            print(error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root, '80657', '')
    root.mainloop()    