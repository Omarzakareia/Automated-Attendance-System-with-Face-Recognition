from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Help:
    def __init__(window, root):
        window.root = root

        # setting tkinter window size
        width = window.root.winfo_screenwidth()
        height = window.root.winfo_screenheight()
        window.root.geometry("%dx%d" % (width, height))
        window.root.title("Face Recognition System")

        # Background image
        img3 = Image.open(r"college_images\bgg.png")
        img3 = img3.resize((1910, 990), Image.Resampling.LANCZOS)
        window.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(window.root, image=window.photoimg3)
        bg_img.place(x=0, y=0, width=1910, height=990)

        title_lbl = Label(bg_img, relief=SOLID, text="Help", font=("times new roman", 30, "bold"), bg="#031888",
                          fg="white")
        title_lbl.place(x=805, y=0, width=300, height=70)

        message_lbl = Label(bg_img, relief=SOLID, text="For any help please message us!",
                            font=("times new roman", 30, "bold"), bg="#031888", fg="white")
        message_lbl.place(x=505, y=300, width=900, height=70)

        Email_lbl = Label(bg_img, relief=SOLID, text="Email: 64390@must.edu.eg",
                          font=("times new roman", 30, "bold"), bg="#031888", fg="white")
        Email_lbl.place(x=505, y=600, width=900, height=70)

        Email_lbl = Label(bg_img, relief=SOLID, text="Email: 80781@must.edu.eg",
                          font=("times new roman", 30, "bold"), bg="#031888", fg="white")
        Email_lbl.place(x=505, y=700, width=900, height=70)

        Email_lbl = Label(bg_img, relief=SOLID, text="Email: 80657@must.edu.eg",
                          font=("times new roman", 30, "bold"), bg="#031888", fg="white")
        Email_lbl.place(x=505, y=500, width=900, height=70)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()