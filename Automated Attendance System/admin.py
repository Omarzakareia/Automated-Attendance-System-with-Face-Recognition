from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
from help import Help
from student import Student


class Admin:
    def __init__(self, root, supervise_id, supervise_name, supervise_type):
        self.root = root
        self.supervise_id = supervise_id
        self.supervise_name = supervise_name
        self.supervise_type = supervise_type

        # setting tkinter window size
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Admin System")

        # background
        img3 = Image.open(r"college_images\white.jpg")
        img3 = img3.resize((1910, 990), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1910, height=990)

        top_frame = LabelFrame(bg_img, bd=2, relief=RIDGE, font=("Calibri", 14, "bold"), bg="#FFFFFF")
        top_frame.place(x=0, y=0, width=1908, height=70)

        title_lbl = Label(self.root, relief=FLAT, text="Administration", font=("Calibri", 25, "bold"), bg="#FFFFFF",
                          fg="Black")
        title_lbl.place(x=30, y=4, width=280, height=60)

        # 1 student button
        img4 = Image.open(r"college_images\info1.png")
        img4 = img4.resize((262, 262))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2", relief=FLAT,
                    bg="#FFFFFF")
        b1.place(x=400, y=350, width=320, height=280)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, relief=RIDGE, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="#e5e5e5", fg="black")
        b1_1.place(x=450, y=630, width=220, height=50)

        # Help button
        img10 = Image.open(r"college_images\help1.jpg")
        img10 = img10.resize((320, 280))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.help_data, relief=FLAT)
        b1.place(x=1200, y=350, width=320, height=280)

        b1_1 = Button(bg_img, text="Help", relief=RIDGE, command=self.help_data, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="#e5e5e5", fg="black")
        b1_1.place(x=1250, y=630, width=220, height=50)

        # 4 Quit button
        b1_1 = Button(bg_img, text="Quit", relief=RIDGE, command=self.quit_app, cursor="hand2",
                      font=("Calibri", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=1730, y=935, width=160, height=50)

        # name
        name_value = Label(bg_img, text=f"Welcome:  {self.supervise_name}", font=("Calibri", 14), bg="#e5e5e5")
        name_value.place(x=1440, y=160, width=400, height=40)



    def quit_app(self):
        self.quit_app = tkinter.messagebox.askyesno("Quit Application", "Are you sure you want to Quit application?",
                                                    parent=self.root)
        if self.quit_app > 0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()