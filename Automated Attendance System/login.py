import tkinter as tk
import cv2
from threading import Thread, Lock
from pathlib import Path
from deepface import DeepFace
import mysql.connector
from admin import Admin
from attend import Attend

num = None
supervise_id = None
supervise_name = None
supervise_type = None

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="T12a34G56",
    database="face_recognizers"
)


class find_face:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)


        self.is_running = False
        self.name = None

    def find(self, *args, **kwargs):
        try:
            c = DeepFace.find(*args, **kwargs)
            

            if c is not None:
                self.name = Path(c[0]['identity'][0]).stem
            else:
                self.name = None
        except Exception as e:
            print("")

        self.is_running = False

    def run(self):
        global supervise_type , supervise_name ,supervise_id
        while not self.name:
            ret, frame = self.cap.read()

            self.find(frame, "superviseimage", enforce_detection=True, distance_metric='euclidean_l2',model_name='ArcFace' ,detector_backend="ssd")

            if self.name is not None:
                print("ID: " + self.name)
                while True:


                    try:
                        connection = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="T12a34G56",
                            database="face_recognizers"
                        )

                        cursor = connection.cursor()
                        query = f"SELECT supervisename ,  supervisetype  FROM supervise WHERE superviseid = {self.name};"
                        cursor.execute(query)
                        result = cursor.fetchone()


                        if result:

                            supervise_id = self.name
                            supervise_name = result[0]
                            supervise_type = result[1]
                        break

                    except mysql.connector.Error as error:
                        print(error)
                        continue

                    finally:
                        if connection.is_connected():
                            cursor.close()
                            connection.close()


class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("500x550+700+200")
        self.resizable(False, False)

        self.layout = tk.Frame(self)
        self.layout.pack(pady=50)

        image = tk.PhotoImage(file="image/info.png")
        photo_label = tk.Label(self.layout)
        photo_label.configure(image=image)
        photo_label.image = image
        photo_label.grid(row=0, column=0, columnspan=2, sticky=tk.N)

        # Username
        username_label = tk.Label(self.layout, text="Username:")
        username_label.grid(row=1, column=0, sticky=tk.W)

        self.username_entry = tk.Text(self.layout, width=50, height=1.5, wrap=tk.NONE)
        self.username_entry.grid(row=2, column=0, padx=10, pady=5)

        # Password
        password_label = tk.Label(self.layout, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.W)

        self.password_entry = tk.Text(self.layout, width=50, height=1.5, wrap=tk.NONE)
        self.password_entry.grid(row=4, column=0, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.layout)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # Login Button
        login_button = tk.Button(button_frame, text="Login", bg="black", fg="white", command=self.login)
        login_button.grid(row=0, column=0, padx=5, pady=10)

        # Photo Button
        photo_button = tk.Button(button_frame, text="Take Photo", bg="black", fg="white", command=self.take_photo)
        photo_button.grid(row=0, column=1, padx=5, pady=10)

        # Center-align the form vertically and horizontally
        self.layout.grid_rowconfigure(0, weight=1)
        self.layout.grid_columnconfigure(0, weight=1)

        self.find = find_face()

    def take_photo(self):
        global supervise_type , supervise_name ,supervise_id
        self.find.run()
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="T12a34G56",
                database="face_recognizers"
            )
            cursor = connection.cursor()

            query = f"SELECT superviseusername FROM supervise WHERE superviseid = '{supervise_id}' "
            
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                if supervise_type == "admin":
                    self.destroy()

                    new_window = tk.Tk()
                    app = Admin(new_window, supervise_id, supervise_name, supervise_type)
                    new_window.mainloop()

                else:
                    self.destroy()
                    new_window = tk.Tk()
                    app = Attend(new_window, supervise_id, supervise_name, supervise_type)
                    new_window.mainloop()

            else:
                print("Invalid username or password")
                self.find.name = None

                supervise_type = None
                supervise_name = None
                supervise_id = None

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            # Close the connection
            if connection.is_connected():
                cursor.close()
                print("MySQL connection closed")

    def login(self):
        global num
        username = self.username_entry.get("1.0", tk.END).strip()
        password = self.password_entry.get("1.0", tk.END).strip()

        # Connect to MySQL database
        try:
            cursor = connection.cursor()

            query = f"SELECT supervisename , superviseid , supervisetype  FROM supervise WHERE superviseusername = '{username}' AND supervisepass = {password}"
            
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                supervise_id = result[1]
                supervise_name = result[0]
                supervise_type = result[2]

                if supervise_type == "admin":
                    self.destroy()

                    new_window = tk.Tk()
                    app = Admin(new_window, supervise_id, supervise_name,supervise_type)
                    new_window.mainloop()

                else:
                    self.destroy()
                    new_window = tk.Tk()
                    app = Attend(new_window, supervise_id, supervise_name, supervise_type)
                    new_window.mainloop()
            else:
                print("Invalid username or password")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            # Close the connection
            if connection.is_connected():
                cursor.close()

                print("MySQL connection closed")


if __name__ == "__main__":
    window = LoginForm()
    window.mainloop()


