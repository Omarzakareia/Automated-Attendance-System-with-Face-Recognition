from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from lec_attend import Lecture
import re
from exam_attend import Exam


class Face_recognition:

    def __init__(self, root, supervise_id, supervise_name):
        self.root=root
        self.supervise_id = supervise_id
        self.supervise_name = supervise_name
        self.n = self
        
        #setting tkinter window size

        self.root.geometry("1910x990+0+0")
        self.root.title("Automated Attendance System")
        # Icon
        p1 = PhotoImage(file = r'college_images\iconn.png')
        self.root.iconphoto(False, p1)
        #background
        img3=Image.open(r"E:\college projects\AAS\college_images\white.jpg")
        img3=img3.resize((1910,990),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1910,height=990)
        #top frame
        top_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=70) 

        title_lbl=Label(bg_img,relief=FLAT,text="Take Attendance using Face",font=("Calibri",25,"normal"),bg="#FFFFFF",fg="black")
        title_lbl.place(x=10,y=4,width=680,height=60)
        
        cent_frame=LabelFrame(bg_img,bd=2,relief=FLAT,font=("Calibri",14,"bold"),bg="white")
        cent_frame.place(x=735,y=300,width=440,height=470)
        self.tr_b = Button(cent_frame, text="Take Attendance lecture", relief=RIDGE, cursor="hand2", command=self.check_lecturers, font=("Calibri", 15, "normal"), bg="#41ba9c", fg="white")
        self.tr_b.place(x=90, y=0, width=250, height=70)
        self.tr_b1 = Button(cent_frame, text="Take Attendance exam", relief=RIDGE, cursor="hand2", command=self.check_exams, font=("Calibri", 15, "normal"), bg="#41ba9c", fg="white")
        self.tr_b1.place(x=90, y=350, width=250, height=70)

    def check_lecturers(self):
        try:
            now = datetime.now()
            lecturers_id = self.supervise_id

            conn = mysql.connector.connect(host="localhost", user="root", password="T12a34G56",
                                           database="face_recognizers")
            cursor = conn.cursor()
            query = f"SELECT lectur1, lectur2, lectur3, lectur4, lectur5, lectur6, lectur7, lectur8, lectur9, lectur10, lectur11, lectur12 FROM lecturer WHERE lecturer_id = {lecturers_id}"

            cursor.execute(query)
            lecturers_data = cursor.fetchone()

            if lecturers_data:
                lectures_starting_soon = []
                time_diffr = []

                for lecture_start_time in lecturers_data:
                    if lecture_start_time:
                        time_diff = lecture_start_time - now

                        if -3600 <= time_diff.total_seconds() <= 600:
                            lectures_starting_soon.append(lecture_start_time.strftime("%Y-%m-%d %H:%M:%S"))
                        if -3600 <= time_diff.total_seconds():
                            time_diffr.append(lecture_start_time.strftime("%Y-%m-%d %H:%M:%S"))

                if lectures_starting_soon:
                    messagebox.showinfo("Upcoming Lectures",
                                        f"The following lectures will start soon:\n{', '.join(lectures_starting_soon)}")
                    time = lectures_starting_soon[0]
                    lectur_fetch = f"SELECT * FROM lecturer WHERE lecturer_id={lecturers_id} AND '{time}' IN (lectur1, lectur2, lectur3, lectur4, lectur5, lectur6, lectur7, lectur8, lectur9, lectur10, lectur11, lectur12); "
                    cursor.execute(lectur_fetch)
                    result = cursor.fetchone()
                    target_datetime = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    index = result.index(target_datetime)
                    print(f"The index of lectur: {index}")
                    lost = ['lecturer_id', 'lecturer_name', 'lecturer_job', 'lectur1', 'lectur2', 'lectur3', 'lectur4',
                            'lectur5', 'lectur6', 'lectur7', 'lectur8', 'lectur9', 'lectur10', 'lectur11', 'lectur12',
                            'coursid']
                    value = lost[index]
                    query_name = f"SELECT coursid FROM lecturer WHERE lecturer_id = {lecturers_id} AND {value} = '{time}'"
                    
                    cursor.execute(query_name)
                    cours_id = cursor.fetchone()
                    query_date_lec = f"SELECT {lost[index]} FROM lecturer WHERE lecturer_id = {lecturers_id} AND coursid = '{cours_id[0]}'"
                    
                    cursor.execute(query_date_lec)
                    lecturers_data = cursor.fetchone()
                    print(cours_id[0], '   ', lecture_start_time)
                    numeric_part = re.findall(r'\d+', value)
                    if numeric_part:
                        number = int(numeric_part[0])
                        new_window = tk.Tk()
                        app = Lecture(new_window, lecturers_id, lecturers_data[0], cours_id[0], number,self.supervise_name)

                else:
                    messagebox.showinfo("Upcoming Lectures",
                                        f"No Upcoming Lectures. The next lecture starts at {time_diffr[0]}")
                    print(f"lectures_starting_soon = {time_diffr}")

            else:
                messagebox.showinfo("No Lectures Found", "No lectures found for the specified lecturer ID.")

        except mysql.connector.Error as error:
            print("Error connecting to MySQL:", error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def check_exams(self):
        try:
            now = datetime.now()
            lecturers_id = self.supervise_id

            conn = mysql.connector.connect(host="localhost", user="root", password="T12a34G56",
                                           database="face_recognizers")
            cursor = conn.cursor()
            query = f"SELECT examdate  FROM exam WHERE superviseid   = {lecturers_id}"

            cursor.execute(query)
            lecturers_data = cursor.fetchone()

            if lecturers_data:
                lectures_starting_soon = []
                time_diffr = []

                for lectur in lecturers_data:

                    if lectur:
                        lecture_start_time = lectur
                        time_diff = lecture_start_time - now

                        if -1200 <= time_diff.total_seconds() <= 600:
                            lectures_starting_soon.append(lecture_start_time.strftime("%Y-%m-%d %H:%M:%S"))
                        if -3600 <= time_diff.total_seconds():
                            time_diffr.append(lecture_start_time.strftime("%Y-%m-%d %H:%M:%S"))

                if lectures_starting_soon:
                    messagebox.showinfo("Upcoming Lectures",
                                        f"The following exam will start soon:\n{', '.join(lectures_starting_soon)}")
                    time = lectures_starting_soon[0]
                    lectur_fetch = f"SELECT  roomid , examname FROM exam  WHERE superviseid ={lecturers_id} AND examdate  ='{time}' ; "
                    cursor.execute(lectur_fetch)
                    result = cursor.fetchone()
                    room = result[0]
                    exam = result[1]
                    query_name = f"SELECT name FROM room WHERE roomid = {room} ;"
                    cursor.execute(query_name)
                    room_name = cursor.fetchone()
                    self.new_window = Toplevel(self.root)
                    self.app = Exam(self.new_window, self.supervise_name, exam, room_name[0])



                else:
                    messagebox.showinfo("Upcoming Lectures",
                                        f"No Upcoming Lectures There are no lectures starting soon. Next lecture start in {time_diffr}")

            else:
                messagebox.showinfo("No Lectures Found", "No lectures found for the specified lecturer ID.")

        except mysql.connector.Error as error:
            print("Error connecting to MySQL:", error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


if __name__ == "__main__":
    root=Tk() 
    obj=Face_recognition(root)
    root.mainloop()   