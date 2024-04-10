import os
import time
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar, DateEntry
import mysql.connector
from deepface import DeepFace
import cv2
from threading import Thread
from pathlib import Path
num = 1
photo = None
photo_status = "college_images/grren.png"
id_row = None


class Exam:

    def __init__(self, root, Invigilator, exam, room):
        self.root = root
        self.Invigilator = Invigilator
        self.exam = exam
        self.room = room

        # setting tkinter window size
        self.root.geometry("1910x990+0+0")

        self.root.title("Automated Attendance System")

        ## Variables
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_attend = StringVar()
        self.var_verify= StringVar()
        self.var_course= StringVar()

        # # Icon
        # p1 = PhotoImage(file=r'college_images\iconn.png')
        # self.root.iconphoto(False, p1)

        # background
        img3 = Image.open(r"E:\college projects\AAS\college_images\white.jpg")
        img3 = img3.resize((1910, 990), Image.Resampling.LANCZOS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)
        # bg_img = Label(self.root, image=self.photoimg3)
        # bg_img.place(x=0, y=0, width=1910, height=990)

        top_frame = LabelFrame( bd=2, relief=RIDGE, font=("Calibri", 14, "bold"), bg="#FFFFFF")
        top_frame.place(x=0, y=0, width=1908, height=70)

        title_lbl = Label(self.root, relief=FLAT, text="Exam Attendance", font=("Calibri", 25, "bold"),
                          bg="#FFFFFF", fg="Black")
        title_lbl.place(x=20, y=4, width=550, height=60)

        # main frame
        main_frm = LabelFrame( relief=RIDGE, bg="white")
        main_frm.place(x=10, y=100, width=1890, height=870)
        # Left Label frame
        left_framee = LabelFrame(main_frm, bd=2, relief=RIDGE, text="Exam Attendance Details",
                                 font=("Calibri", 14, "bold"), bg="White")
        left_framee.place(x=10, y=40, width=920, height=700)

        left_first_frame = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_first_frame.place(x=15, y=15, width=880, height=120)

        left_second_frame = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_second_frame.place(x=15, y=103, width=880, height=340)

        left_third_frame = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_third_frame.place(x=15, y=441, width=880, height=220)

        # exam name
        exa_label = Label(left_first_frame, text=f"Room : {self.room}", font=("Calibri", 14, "bold"))
        exa_label.place(x=700, y=35,  height=30)



        self.photo_status_label = Label(left_first_frame, font=("Calibri", 14, "bold"))
        self.photo_status_label.place(x=850, y=35, height=30)


        # date
        exam_name = Label(left_first_frame, text=f"Exam Name : {self.exam}", font=("Calibri", 14, "bold"))
        exam_name.place(x=310, y=35,  height=30)


        # invigilator
        exam_invigilator = Label(left_first_frame, text=f"Exam Invigilator : {self.Invigilator}", font=("Calibri", 14, "bold"))
        exam_invigilator.place(x=15, y=35,  height=30)

        self.image_label = Label(left_second_frame, relief=RIDGE, font=("Calibri", 14, "bold"), bg="white")
        self.image_label.place(x=25, y=15, width=420, height=300)

        take_photo = Button(left_second_frame, text="Take Photo", relief=RIDGE, cursor="hand2",
                            font=("Calibri", 15, "bold"), bg="#235e51", fg="white" , command=self.check_face)
        take_photo.place(x=470, y=35, width=180, height=50)

        self.Id_label = Label(left_second_frame, text="ID:", font=("Calibri", 15, "bold"), bg="#90EE90")
        self.Id_label.place(x=470, y=125, height=40)

        Verify = Button(left_second_frame, text="Verify", relief=RIDGE, cursor="hand2",
                            font=("Calibri", 15, "bold"), bg="#235e51", fg="white",command=self.verfiy)
        Verify.place(x=470, y=215, width=180, height=50)
        # 3 third frame
        # student name
        student_name = Label(left_third_frame, text="Student Name:", font=("Calibri", 14, "bold"), bg="#90EE90")
        student_name.place(x=15, y=25, width=120, height=30)
        student_name_entry = ttk.Entry(left_third_frame, width=20,textvariable=self.var_name)
        student_name_entry.place(x=145, y=25, width=250, height=30)

        # student id
        student_id = Label(left_third_frame, text="Student ID:", font=("Calibri", 14, "bold"), bg="#90EE90")
        student_id.place(x=430, y=25, width=120, height=30)
        student_id_entry = ttk.Entry(left_third_frame, width=20,textvariable=self.var_student_id)
        student_id_entry.place(x=560, y=25, width=250, height=30)
        # course name
        course_name = Label(left_third_frame, text="Course Name:", font=("Calibri", 14, "bold"), bg="#90EE90")
        course_name.place(x=15, y=85, width=120, height=30)
        course_name_entry = ttk.Entry(left_third_frame, width=20,textvariable=self.var_course)
        course_name_entry.place(x=145, y=85, width=250, height=30)
        # attend
        attend_label = Label(left_third_frame, text="Attendance:", font=("Calibri", 14, "bold"), bg="#90EE90")
        attend_label.place(x=430, y=85,  height=30)

        self.attend_combo = ttk.Combobox(left_third_frame,textvariable=self.var_attend, font=("Calibri", 12, "normal"), state="readonly")
        self.attend_combo["values"] = ("Yes", "No")
        self.attend_combo.place(x=560, y=85, width=100, height=30)

        verify_label = Label(left_third_frame, text="verify:", font=("Calibri", 14, "bold"), bg="#90EE90")
        verify_label.place(x=670, y=85,  height=30)

        self.verify_combo = ttk.Combobox(left_third_frame, textvariable=self.var_verify, font=("Calibri", 12, "normal"),
                                         state="readonly")
        self.verify_combo["values"] = ("Yes", "No")
        self.verify_combo.place(x=730, y=85, width=100, height=30)

        # save button
        save_b = Button(left_third_frame, text="Save", relief=RIDGE, cursor="hand2", font=("Calibri", 15, "bold"),
                        bg="#235e51", fg="white",command=self.check_manual)
        save_b.place(x=350, y=145, width=130, height=50)

        # 4 Quit button
        quit_b = Button( text="End", command=self.quit_app, relief=RIDGE, cursor="hand2",
                        font=("Calibri", 15, "bold"), bg="red", fg="white")
        quit_b.place(x=900, y=895, width=160, height=50)
        # Start button
        startb = Button( text="Start", relief=RIDGE, cursor="hand2",
                        font=("Calibri", 15, "bold"), bg="red", fg="white" , command=self.start)
        startb.place(x=1500, y=895, width=160, height=50)

        # Right Label frame
        right_framee = LabelFrame(main_frm, bd=2, relief=RIDGE, text="Attendance Details", font=("Calibri", 14, "bold"),
                                  bg="white")
        right_framee.place(x=950, y=40, width=915, height=700)
        table_frm = Frame(right_framee, bd=2, relief=RIDGE, bg="white")
        table_frm.place(x=15, y=130, width=880, height=520)

        # search system
        search_frame = LabelFrame(right_framee, bd=2, relief=RIDGE, text="Search System", font=("Calibri", 14, "bold"),
                                  bg="white")
        search_frame.place(x=60, y=5, width=690, height=100)
        search_label = Label(search_frame, text="Search By:", font=("Calibri", 14, "bold"), bg="#90EE90")
        search_label.grid(row=0, column=0, padx=20, pady=20, sticky=W)

        self.search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=0, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(search_frame, font=("Calibri", 12, "normal"), state="readonly")
        self.search_combo["values"] = ("Student Name", "Student ID")
        self.search_combo.grid(row=0, column=3, padx=10)

        search_btn = Button(search_frame, text="Search", width=10, font=("Calibri", 13, "normal"), bg="#235e51",
                            fg="white", command=self.search_in_database)
        search_btn.grid(row=0, column=4, padx=15)



        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)
        self.AttendReportTable = ttk.Treeview(table_frm,
                                              column=("std_name", "std_id", "course", "attend", "verify"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=24)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendReportTable.xview)
        scroll_y.config(command=self.AttendReportTable.yview)

        self.AttendReportTable.heading("std_name", text="Student ID")
        self.AttendReportTable.heading("std_id", text="Student Name")
        self.AttendReportTable.heading("course", text="Course Name")
        self.AttendReportTable.heading("attend", text="Camera Attend")
        self.AttendReportTable.heading("verify", text="Verify Attend")
        self.AttendReportTable["show"] = "headings"

        self.AttendReportTable.column("std_name", width=120, anchor=CENTER)
        self.AttendReportTable.column("std_id", width=120, anchor=CENTER)
        self.AttendReportTable.column("course", width=120, anchor=CENTER)
        self.AttendReportTable.column("attend", width=120, anchor=CENTER)
        self.AttendReportTable.column("verify", width=120, anchor=CENTER)
        self.AttendReportTable.tag_configure('odd_row', background='white')
        self.AttendReportTable.tag_configure('even_row', background='#808080')
        self.AttendReportTable.pack(fill=BOTH, expand=1)
        self.AttendReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fill_table()
        Thread(target=self.update_attendance).start()


    def start(self):
        Thread(target=self.update_attendance).start()

    def quit_app(self):
        self.quit_app = tkinter.messagebox.askyesno("Quit Application", "Are you sure you want to Quit application?",
                                                    parent=self.root)
        if self.quit_app > 0:
            for row_id in self.AttendReportTable.get_children():
                values = self.AttendReportTable.item(row_id)['values']
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="T12a34G56",
                        database="face_recognizers"
                    )
                    if len(values) != 5:
                        cursor = connection.cursor()
                        query = f"UPDATE {self.exam} SET Attend_camera = '0' AND Attend_verify = '0'  WHERE studentid = {str(values[0])};"
                        cursor.execute(query)
                        print(query)

                    else:
                        print(len(values))
                        cursor = connection.cursor()
                        query = f"UPDATE {self.exam} SET Attend_camera = '1' AND Attend_verify = '1'  WHERE studentid = {str(values[0])};"
                        print(query)
                        cursor.execute(query)

                except mysql.connector.Error as error:
                    print(error)
                finally:
                    connection.commit()

            self.root.destroy()
        else:
            return

    def update_attendance(self):
        global photo_status
        photo_status= "college_images/grren.png"
        image_path = photo_status
        image = Image.open(image_path)
        image = image.resize((20, 20), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.photo_status_label.config(image=photo)
        self.photo_status_label.image = photo
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(3, 640)
        cap.set(4, 420)

        name = None
        while True:

            ret, frame = cap.read()

            if not ret:
                # Frame retrieval failed, handle the error
                print("Failed to retrieve frame from the camera")
                continue


            try:
                c = DeepFace.find(frame, "superviseimage", enforce_detection=False, model_name='Facenet512')
                print(c)

                if c is not None:
                    name = Path(c[0]['identity'][0]).stem
                else:
                    name = None

            except Exception as e:
                print(e)

            if name is not None:
                entered_id = name
                items = self.AttendReportTable.get_children()
                for item in items:
                    student_id = self.AttendReportTable.item(item)["values"][0]
                    if str(student_id) == str(entered_id):
                        self.AttendReportTable.set(item, "attend", "1")
                        break
            name = None

    def mark_empty_rows(self):
        for row_id in self.AttendReportTable.get_children():
            values = self.AttendReportTable.item(row_id)['values']
            for value in values:
                if len(str(value).strip()) <= 3:
                    self.AttendReportTable.item(row_id, tags=('odd_row',))
                    break
            else:
                self.AttendReportTable.item(row_id, tags=('even_row',))


    def search_in_database(self):
        def select(item_serch, item_comper):
            for row in self.AttendReportTable.get_children():
                value = self.AttendReportTable.item(row, 'values')
                if value[item_serch] == item_comper:
                    self.AttendReportTable.selection_clear()
                    self.AttendReportTable.focus(None)
                    self.AttendReportTable.selection_set(row)
                    self.AttendReportTable.focus(row)
                    self.AttendReportTable.see(row)
                    break

        selected_combo = self.search_combo.get()
        search_text = self.search_entry.get()
        if search_text is None and selected_combo is None:
            messagebox.showinfo("Warning",
                                "No information for search  ")
        else:
            if selected_combo == "Student Name":
                select(1, search_text)

            elif selected_combo == "Student ID":
                select(0, search_text)



    def check_manual(self):
        selected_combo_attend = self.attend_combo.get()
        selected_combo_verify = self.verify_combo.get()
        print(f"{selected_combo_attend}")
        if selected_combo_attend is None and self.var_student_id is None or selected_combo_verify is None and self.var_student_id  is None:
            messagebox.showinfo("Warning",
                                "No enough information for to modify")
        else:

            if selected_combo_verify == "Yes":

                for row in self.AttendReportTable.get_children():
                    value = self.AttendReportTable.item(row, 'values')
                    if value[0] == self.var_student_id.get():
                        print(self.var_student_id)
                        self.AttendReportTable.set(row, "attend", "1")
                        self.AttendReportTable.set(row, "verify", "1")
                        break

            elif selected_combo_attend == "Yes":
                for row in self.AttendReportTable.get_children():
                    value = self.AttendReportTable.item(row, 'values')
                    if value[0] == self.var_student_id.get():
                        self.AttendReportTable.set(row, "attend", "1")
                        break

    def fill_table(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()
            query = f"SELECT studentid, studentname, coursid FROM {self.exam}"
            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                student_id = row[0]
                student_name = row[1]
                coursid = row[2]
                query = f"SELECT code FROM cours WHERE coursid = {coursid}"
                cursor.execute(query)
                result1 = cursor.fetchall()

                course_codes = []

                for code_row in result1:
                    course_code = code_row[0]
                    course_codes.append(course_code)

                course_codes_str = ', '.join(course_codes)

                self.AttendReportTable.insert("", "end", values=(student_id, student_name, course_codes_str))

        except mysql.connector.Error as error:
            print(error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_cursor(self, event=""):
        cursor_focus = self.AttendReportTable.focus()
        content = self.AttendReportTable.item(cursor_focus)
        data = content["values"]
        self.var_name.set(data[1]),
        self.var_student_id.set(data[0]),
        self.var_course.set(data[2]),
        if data[0] is not None:
            image_path = f"superviseimage/{data[0]}.png"
            image = Image.open(image_path)
            image = image.resize((440, 260), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.Id_label.config(text=f"ID: {data[0]}")
        else:
            self.image_label.config(image="")
            self.Id_label.config(text="")

    def check_face(self):
        global id_row , photo_status
        photo_status="college_images/Red-Circle.png"
        image_path = photo_status
        image = Image.open(image_path)
        image = image.resize((20, 20), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.photo_status_label.config(image=photo)
        self.photo_status_label.image = photo

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(3, 640)
        cap.set(4, 420)

        iterations = 0
        while iterations < 100:
            name = None  # Reset name to None before each iteration

            ret, frame = cap.read()

            if not ret:
                print("Failed to retrieve frame from the camera")
                break
            try:
                c = DeepFace.find(frame, "superviseimage", enforce_detection=False, model_name='Facenet512')
                print(c)
                if c is not None:
                    name = Path(c[0]['identity'][0]).stem
                else:
                    name = None

            except Exception as e:
                print(e)

            if name is not None:
                id = name
                photo_path = f"superviseimage/{name}.png"
                if os.path.isfile(photo_path):
                    image = Image.open(photo_path)
                    image = image.resize((420, 300))
                    photo = ImageTk.PhotoImage(image)
                    self.image_label.config(image=photo)
                    self.image_label.photo = photo
                    self.Id_label.config(text=f"ID: {id}")
                    photo_status = "college_images/grren.png"
                    image_path = photo_status
                    image = Image.open(image_path)
                    image = image.resize((20, 20), Image.ANTIALIAS)
                    photo = ImageTk.PhotoImage(image)
                    self.photo_status_label.config(image=photo)
                    for row in self.AttendReportTable.get_children():
                        value = self.AttendReportTable.item(row, 'values')
                        if value[0] == id:
                            self.AttendReportTable.selection_set(row)
                            self.AttendReportTable.focus(row)
                            self.AttendReportTable.see(row)
                            id_row = value[0]
                            break

                    break

            iterations += 1

        if iterations == 100 and name is None:
            messagebox.showinfo("Warning", " We did not find this face in the records. Please check it by checking the ID or try again you must click on start butten to Continuing the process of preparing students")
        cap.release()

    def verfiy(self):
        global id_row
        if id_row is None:messagebox.showinfo("warning",
                                "ther is no id to verify")

        else:
            for row in self.AttendReportTable.get_children():
                value = self.AttendReportTable.item(row, 'values')
                if value[0] == id_row:
                    self.AttendReportTable.set(row, "attend", "1")
                    self.AttendReportTable.set(row, "verify", "1")
                else:
                    messagebox.showinfo("Warning",
                                        f"Theres no student by this ID : {id_row} in this exam")


if __name__ == "__main__":
    root = Tk()
    obj = Exam(root)
    root.mainloop()