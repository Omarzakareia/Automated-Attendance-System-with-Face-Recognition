from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
from help import Help
from attendance import Attendance
from face_recognition import Face_recognition



class Attend:
    def __init__(self, root, supervise_id, supervise_name, supervise_type):
        self.root = root
        self.supervise_id = supervise_id
        self.supervise_name = supervise_name
        self.supervise_type = supervise_type




        # setting tkinter window size
        self.root.geometry("1910x990+0+0")

        self.root.title("Face Recognition System")


        # background
        img3 = Image.open(r"college_images\white.jpg")
        img3 = img3.resize((1910, 990), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1910, height=990)

        top_frame = LabelFrame(bg_img, bd=2, relief=RIDGE, font=("Calibri", 14, "bold"), bg="#FFFFFF")
        top_frame.place(x=0, y=0, width=1908, height=70)

        title_lbl = Label(self.root, relief=FLAT, text="Lecturer", font=("Calibri", 25, "bold"), bg="#FFFFFF",
                          fg="Black")
        title_lbl.place(x=30, y=4, width=280, height=60)

        # 1 student button
        img5 = Image.open(r"college_images\detect.jpg")
        img5 = img5.resize((320, 280))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.face_reco, cursor="hand2", relief=FLAT, bg="#FFFFFF")
        b1.place(x=280, y=350, width=320, height=280)

        b1_1 = Button(bg_img, text="Take Attendance", command=self.face_reco, relief=RIDGE, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="#e5e5e5", fg="black")
        b1_1.place(x=330, y=625, width=220, height=50)

        # 2
        img6 = Image.open(r"college_images\attend.png")
        img6 = img6.resize((320, 280))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, command=self.attend, cursor="hand2", relief=FLAT, bg="#FFFFFF")
        b1.place(x=825, y=350, width=320, height=280)

        b1_1 = Button(bg_img, text="Attendance Details", command=self.attend, relief=RIDGE, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="#e5e5e5", fg="black")
        b1_1.place(x=870, y=625, width=220, height=50)

        # Help button
        img10 = Image.open(r"college_images\help1.jpg")
        img10 = img10.resize((320, 280))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", relief=FLAT)
        b1.place(x=1400, y=350, width=320, height=280)

        b1_1 = Button(bg_img, text="Help", relief=RIDGE, cursor="hand2", command=self.help_data,
                      font=("Calibri", 15, "bold"), bg="#e5e5e5", fg="black")
        b1_1.place(x=1450, y=625, width=220, height=50)

        # 4 Quit button
        b1_1 = Button(bg_img, text="Quit", relief=RIDGE, command=self.quit_app, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=1730, y=935, width=160, height=50)

        # name
        name_label = Label(bg_img, text=f"Welcome : {self.supervise_name}", font=("Calibri", 14, "bold"), bg="white")
        name_label.place(x=1300, y=120, width=400, height=50)
        # role
        role_label = Label(bg_img, text=f"Role : {self.supervise_type}", font=("Calibri", 14, "bold"), bg="white")
        role_label.place(x=1300, y=170, width=400, height=50)



    def quit_app(self):
        self.quit_app = tkinter.messagebox.askyesno("Quit Application", "Are you sure you want to Quit application?",
                                                    parent=self.root)
        if self.quit_app > 0:
            self.root.destroy()
        else:
            return

    def attend(self):
        self.new_window = Toplevel(self.root)

        self.app = Attendance(self.new_window,self.supervise_id,self.supervise_name)

    def face_reco(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window,self.supervise_id,self.supervise_name)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Attend(root)
    root.mainloop()    