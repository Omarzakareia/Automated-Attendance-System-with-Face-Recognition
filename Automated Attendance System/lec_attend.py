from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from deepface import DeepFace
import cv2
from threading import Thread
from pathlib import Path

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="T12a34G56",
    database="face_recognizers"
)


class Lecture:
    def __init__(self, root, lecturer_id, lectur, cours_id, number,supervise_name):
        self.root=root
        self.lecturers_id =lecturer_id
        self.lectur = lectur
        self.cours_id = cours_id
        self.number = number
        self.supervise_name = supervise_name

        # setting tkinter window size


        ## Variables
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_attend = StringVar()


        cursor = connection.cursor()
        query_name_cours = f"SELECT code FROM cours WHERE coursid = {self.cours_id}"
        cursor.execute(query_name_cours)
        result = cursor.fetchone()




        # Icon
        # p1 = PhotoImage(file=r'college_images\iconn.png')
        # self.root.iconphoto(False, p1)

        self.root.geometry("1910x990+0+0")
        self.root.title("Lecture Attendance System")
        # background
        backg = Image.open(r"college_images\white.jpg")
        backg = backg.resize((1910, 990), Image.Resampling.LANCZOS)
        photoimgbg = ImageTk.PhotoImage(backg)
        bg_img1 = Label( image=photoimgbg)
        bg_img1.place(x=0, y=0, width=1910, height=990)
        
        

        top_frame = LabelFrame(bg_img1, bd=2, relief=RIDGE, font=("Calibri", 14, "bold"), bg="#FFFFFF")
        top_frame.place(x=0, y=0, width=1908, height=70)

        title_lbl = Label(bg_img1, relief=FLAT, text="Lecture Attendance", font=("Calibri", 25, "bold"),
                          bg="#FFFFFF", fg="Black")
        title_lbl.place(x=20, y=4, width=550, height=60)


        # Left Label frame
        left_framee = LabelFrame(bg_img1, bd=2, relief=RIDGE, text="Lecture Attendance Details",
                                 font=("Calibri", 14, "bold"), bg="White")
        left_framee.place(x=10, y=10, width=920, height=700)

        left_small_frame = LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_small_frame.place(x=15, y=15, width=880, height=250)
        
        left_two_frame= LabelFrame(left_framee, bd=2, relief=RIDGE, bg="white")
        left_two_frame.place(x=15, y=350, width=880, height=240)
        
        lec_lab1 = Label(left_small_frame, text=f"Lecture Name : {self.cours_id}", font=("Calibri", 15, "bold"), bg="white")
        lec_lab1.place(x=30 , y= 20  )

        name_label = Label(left_small_frame, text=f"Lecture No : {self.number}", font=("Calibri", 15, "bold"), bg="white")
        name_label.place(x=400 , y= 15  )

        dat_label = Label(left_small_frame, text=f"Lecture Date : {self.lectur}", font=("Calibri", 15, "bold"), bg="white")
        dat_label.place(x=30,y=115)

        lecr_label = Label(left_small_frame, text=f"Lecturer Name : {self.supervise_name}", font=("Calibri", 15, "bold"), bg="white")
        lecr_label.place(x=400,y=115)

        names_label = Label(left_two_frame, text="Student Name:", font=("Calibri", 14, "bold"), bg="#90EE90")
        names_label.grid(row=5, column=0, padx=15, pady=20)
        names_entry = ttk.Entry(left_two_frame, textvariable=self.var_name, width=20, font=("Calibri", 14, "bold"),
                                state="readonly")
        names_entry.grid(row=5, column=1, pady=20, sticky=W)

        ids_label = Label(left_two_frame, text="Student ID:", font=("Calibri", 14, "bold"), bg="#90EE90")
        ids_label.grid(row=5, column=2, padx=15)
        self.ids_entry = ttk.Entry(left_two_frame, textvariable=self.var_student_id, width=20, font=("Calibri", 14, "bold"),
                              state="readonly")
        self.ids_entry.grid(row=5, column=3, pady=20, sticky=W)

        self.attend_label = Label(left_two_frame, text="Attend", font=("Calibri", 14, "bold"), bg="#90EE90")
        self.attend_label.grid(row=6, column=0, padx=5)
        self.attend_combo = ttk.Combobox(left_two_frame, textvariable=self.var_attend, font=("Calibri", 12, "normal"),
                                    state="readonly")
        self.attend_combo["values"] = ("Yes", "No")
        self.attend_combo.grid(row=6, column=1, padx=12, pady=25, sticky=W)


        # 4 Quit button
        quit_b = Button( text="End", command = self.quit_app, relief=RIDGE, cursor="hand2",
                        font=("Calibri", 15, "bold"), bg="red", fg="white")
        quit_b.place(x=900, y=865, width=160, height=50)

        # save button
        save_b = Button(left_two_frame, text="Save", relief=RIDGE, cursor="hand2",command=self.verfiy,
                      font=("Calibri", 20, "bold"), bg="red", fg="white")
        save_b.grid(row=7, column=2, padx=112, pady=25, sticky=W)

        # Right Label frame
        right_framee = LabelFrame(bg_img1, bd=2, relief=RIDGE, text="Attendance Details", font=("Calibri", 14, "bold"),
                                  bg="white")
        right_framee.place(x=950, y=10, width=915, height=700)
        table_frm = Frame(right_framee, bd=2, relief=RIDGE, bg="white")
        table_frm.place(x=15, y=130, width=880, height=520)

        # search system
        search_frame = LabelFrame(right_framee, bd=2, relief=RIDGE, text="Search System", font=("Calibri", 14, "bold"),
                                  bg="white")
        search_frame.place(x=60, y=5, width=700, height=100)
        search_label = Label(search_frame, text="Search By:", font=("Calibri", 14, "bold"), bg="#90EE90")
        search_label.grid(row=0, column=0, padx=20, pady=20, sticky=W)

        self.search_combo = ttk.Combobox(search_frame, font=("Calibri", 12, "normal"), state="readonly")
        self.search_combo["values"] = ("Student Name", "Student ID")
        self.search_combo.grid(row=0, column=4, padx=10)

        self.search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=0, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=("Calibri", 13, "normal"), bg="#000000",
                            fg="white",command=self.search_in_database)
        search_btn.grid(row=0, column=3, padx=15)



        #### scroll bar for the right frame
        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)
        self.AttendReportTable = ttk.Treeview(table_frm, column=("id", "name", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=24)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendReportTable.xview)
        scroll_y.config(command=self.AttendReportTable.yview)

        self.AttendReportTable.heading("id", text="Student ID")
        self.AttendReportTable.heading("name", text="Student Name")
        self.AttendReportTable.heading("attendance", text="Attendance")
        self.AttendReportTable["show"] = "headings"

        self.AttendReportTable.column("id", width=100, anchor=CENTER)
        self.AttendReportTable.column("name", width=120, anchor=CENTER)
        self.AttendReportTable.column("attendance", width=100, anchor=CENTER)
        self.AttendReportTable.tag_configure('odd_row', background='white')
        self.AttendReportTable.tag_configure('even_row', background='#808080')

        self.fill_table()
        self.AttendReportTable.pack(fill=BOTH, expand=1)

        Thread(target=self.update_attendance).start()
        self.AttendReportTable.bind("<ButtonRelease>",self.get_cursor)

    def quit_app(self):
        self.quit_app = tkinter.messagebox.askyesno("Quit Application", "Are you sure you want to Quit application?", parent=self.root)
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
                    if len(values) != 3:
                        cursor = connection.cursor()
                        query = f"UPDATE {self.cours_id} SET lectur{self.number} = '0' WHERE studentid = {str(values[0])};"
                        cursor.execute(query)
                        print(query)

                    else:
                        print(len(values))
                        cursor = connection.cursor()
                        query = f"UPDATE {self.cours_id} SET lectur{self.number} = '1' WHERE studentid = {str(values[0])};"
                        print(query)
                        cursor.execute(query)

                except mysql.connector.Error as error:
                    print(error)
                finally:
                    connection.commit()

            self.root.destroy()
        else:
            return

    def fill_table(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()
            query = "SELECT studentid, studentname FROM cse500"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                student_id = row[0]
                student_name = row[1]
                self.AttendReportTable.insert("", "end", values=(student_id, student_name))

        except mysql.connector.Error as error:
            print(error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    import cv2
    from PIL import Image, ImageTk

    # ...

    def update_attendance(self):
        cap = cv2.VideoCapture(0)

        # Create a Tkinter window for displaying the camera view

        name = None
        while True:

            ret, frame = cap.read()

            if not ret:
                # Frame retrieval failed, handle the error
                print("Failed to retrieve frame from the camera")
                break

            try:
                c = DeepFace.find(frame, "superviseimage", enforce_detection=True,distance_metric='euclidean_l2' ,detector_backend="ssd",model_name='ArcFace')
                

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
                        self.AttendReportTable.set(item, "attendance", "1")
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
    # def mark_empty_rows(self):
    #     for row_id in self.AttendReportTable.get_children():
    #         values = self.AttendReportTable.item(row_id)['values']
    #         num_values = len(values)
    #         print(num_values)
    #         if num_values < 3:
    #             self.AttendReportTable.item(row_id, tags=('odd_row',))
    #             print("111111111111111111111111111111111")
    #
    #         else:
    #             self.AttendReportTable.item(row_id, tags=('even_row',))
    #             print("4655454545454")

    def get_cursor(self, event=""):
        cursor_focus = self.AttendReportTable.focus()
        content = self.AttendReportTable.item(cursor_focus)
        data = content["values"]
        self.var_student_id.set(data[0])
        self.var_name.set(data[1])
        

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

        selected_combo = self.search_combo.get()
        search_text = self.search_entry.get()
        if search_text is None and selected_combo is None:
            messagebox.showinfo("Warning",
                                "No information for search  ")
        else:
            if selected_combo == "Student Name":
                select(1, search_text)
                print(selected_combo)

            elif selected_combo == "Student ID":
                select(0, search_text)
                print(selected_combo)


    def verfiy(self):

        selected_combo_attend = self.attend_combo.get()
        id_row=self.ids_entry.get()

        if selected_combo_attend is None and id_row is None:
            messagebox.showinfo("warning","ther is no enough data to save")

        else:

            id_found = False  # Flag to keep track of whether the ID is found in the loop

            for row in self.AttendReportTable.get_children():

                value = self.AttendReportTable.item(row, 'values')

                if value[0] == id_row:
                    self.AttendReportTable.set(row, "attendance", "1")

                    id_found = True  # Set the flag to True if ID is found

                    break

            if not id_found:
                messagebox.showinfo("Warning", f"There is no student with ID: {id_row} in this lecture")




if __name__ == "__main__":
    root = Tk()
    obj = Lecture(root, "", "", "",'')
    root.mainloop()