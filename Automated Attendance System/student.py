from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

photo=None
    
class Student:
    def __init__(window,root):
        window.root=root
        
        #setting tkinter window size

        window.root.geometry("1910x990+0+0")
        window.root.title("Face Recognition System") 
        
        #variables
        window.var_dep=StringVar()
        window.var_year=StringVar()
        window.var_std_id=StringVar()
        window.var_gender=StringVar()
        window.var_email=StringVar()
        window.var_phone=StringVar()
        window.var_name=StringVar()
        window.var_radio1=StringVar()
        window.var_super="80781"
          
        # Icon
        p1 = PhotoImage(file = r'E:\college projects\AAS\college_images\iconn.png')
        window.root.iconphoto(False, p1)
        # Background image
        img3=Image.open(r"E:\college projects\AAS\college_images\white.jpg")
        img3=img3.resize((1910,990),Image.Resampling.LANCZOS)
        window.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(window.root,image=window.photoimg3)
        bg_img.place(x=0,y=0,width=1910,height=990)
        #top Frame
        top_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=60) 
        title_lbl=Label(bg_img,relief=SOLID,text="Student Management System",font=("Calibri",20,"normal"),bg="#FFFFFF",fg="black")
        title_lbl.place(x=705,y=0,width=500,height=60) 
        
        #Left Label frame
        left_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Student Registeration",font=("Calibri",14,"bold"),bg="white")
        left_frame.place(x=10,y=100,width=940,height=870)
        
        
        #current course info
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course information",font=("Calibri",14,"bold"),bg="white")
        current_course_frame.place(x=20,y=30,width=900,height=150) 
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("Calibri",14,"bold"),bg="#90EE90")
        dep_label.grid(row=0,column=0,padx=5)
        dep_combobox=ttk.Combobox(current_course_frame,textvariable=window.var_dep,font=("Calibri",12,"normal"),state="readonly")
        dep_combobox["values"]=("Select Department","Computer","Civil","Mechatronics","Communication","Mechanical")
        dep_combobox.current(0)
        dep_combobox.grid(row=0,column=1,padx=12,pady=25,sticky=W)   
        

      
 
           
        #Year
        year_label=Label(current_course_frame,text="Year",font=("Calibri",14,"bold"),bg="#90EE90")
        year_label.grid(row=0,column=2)
        year_combobox=ttk.Combobox(current_course_frame,textvariable=window.var_year,font=("Calibri",12,"normal"),state="readonly")
        year_combobox["values"]=("Select Year","2022-2023","2023","2023-2024","2024","2024-2025")
        year_combobox.current(0)
        year_combobox.grid(row=0,column=3,pady=20,padx=15,sticky=W)           
        
        
        
        #Class Student info
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("Calibri",14,"bold"),bg="white")
        class_student_frame.place(x=20,y=200,width=900,height=620)  

       #name
        name_label=Label(class_student_frame,text="Name:",font=("Calibri",14,"bold"),bg="#90EE90")
        name_label.grid(row=0,column=0,padx=5)   
        name_entry=ttk.Entry(class_student_frame,textvariable=window.var_name,width=20,font=("Calibri",14,"bold"))          
        name_entry.grid(row=0,column=1,pady=20,sticky=W)   
        
        #photo label
        window.photo_label=Label(class_student_frame,bg="white",relief=RIDGE)
        window.photo_label.place(x=40,y=185,width=440,height=260)
        
        #student ID
        stud_id_label=Label(class_student_frame,text="Student-ID:",font=("Calibri",14,"bold"),bg="#90EE90")
        stud_id_label.grid(row=0,column=2,padx=5)   
        stud_id_entry=ttk.Entry(class_student_frame,textvariable=window.var_std_id,width=20,font=("Calibri",14,"bold"))          
        stud_id_entry.grid(row=0,column=3,pady=20,sticky=W)        
                     
       #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("Calibri",14,"bold"),bg="#90EE90")
        gender_label.grid(row=2,column=0,padx=5)           
        gender_combo=ttk.Combobox(class_student_frame,textvariable=window.var_gender,font=("Calibri",12,"normal"),state="readonly",width=15)
        gender_combo["values"]=("Select Gender","Male","Female")   
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)      
       
    
       
       #phone
        phone_label=Label(class_student_frame,text="Phone:",font=("Calibri",14,"bold"),bg="#90EE90")
        phone_label.grid(row=1,column=0,padx=5)   
        phone_entry=ttk.Entry(class_student_frame,textvariable=window.var_phone,width=20,font=("Calibri",14,"bold"))          
        phone_entry.grid(row=1,column=1,pady=20,sticky=W)       
              
       #email
        email_label=Label(class_student_frame,text="Email:",font=("Calibri",14,"bold"),bg="#90EE90")
        email_label.grid(row=1,column=2,padx=5)   
        email_entry=ttk.Entry(class_student_frame,textvariable=window.var_email,width=20,font=("Calibri",14,"bold"))          
        email_entry.grid(row=1,column=3,pady=20,sticky=W)        
        

        
        #buttons frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=FLAT,bg="white")
        btn_frame.place(x=50,y=460,width=830,height=47)
        
        window.save_btn=Button(btn_frame,text="Save",command=window.add_data,width=13,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        window.save_btn.grid(row=0,column=0,padx=10)

        update_btn=Button(btn_frame,text="Update",command=window.update_data,width=14,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=window.delete_data,width=14,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",command=window.reset_data,width=14,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        reset_btn.grid(row=0,column=4,padx=15)   
          
        update_b=Button(btn_frame,text="Update with Photo",command=window.update_data_photo,width=20,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        update_b.grid(row=0,column=2,padx=20)
                   
        btn_frame1=Frame(class_student_frame,bd=2,relief=FLAT,bg="white")
        btn_frame1.place(x=150,y=520,width=590,height=47)
        
        takephoto_btn=Button(btn_frame1,text="Take Photo Sample",command=window.generate_dataset,width=25,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        takephoto_btn.grid(row=0,column=0,padx=180)





        #Right Label frame
        right_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Student Details",font=("Calibri",14,"bold"),bg="white")
        right_frame.place(x=960,y=100,width=940,height=870)       
        
        #search system
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("Calibri",14,"bold"),bg="white")
        search_frame.place(x=20,y=15,width=900,height=120)       
        search_label=Label(search_frame,text="Search By:",font=("Calibri",14,"bold"),bg="#90EE90")
        search_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("Calibri",14,"normal"),state="readonly",width=15)
        search_combo["values"]=("Select","Student_id","Student_Name")   
        search_combo.current(0)        
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 
        
        search_entry=ttk.Entry(search_frame,width=20,font=("Calibri",13,"bold"))          
        search_entry.grid(row=0,column=2,padx=15,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=10,font=("Calibri",13,"normal"),bg="#000000",fg="white")
        search_btn.grid(row=0,column=3,padx=8)
        
        showAll_btn=Button(search_frame,text="Show all",width=10,font=("Calibri",13,"normal"),bg="#000000",fg="white")
        showAll_btn.grid(row=0,column=4,padx=8)
        
        # Back button
        b1_1=Button(bg_img,text="Back",relief=RIDGE,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=1720,y=5,width=140,height=50)
        
        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=20,y=160,width=900,height=640)  
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
  
        window.student_table=ttk.Treeview(table_frame,column=("studentid","studentname","studentyear","studentgender","studendepartment","studentemail","studentphone","studentimage","superviseid"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        s=ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=24)    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=window.student_table.xview)
        scroll_y.config(command=window.student_table.yview)
        
        window.student_table.heading("studentid",text="Student_id")
        window.student_table.heading("studentname",text="Student Name")
        window.student_table.heading("studentyear",text="Student year")
        window.student_table.heading("studentgender",text="Student gender") 
        window.student_table.heading("studendepartment",text="Department")
        window.student_table.heading("studentemail",text="Email")
        window.student_table.heading("studentphone",text="Phone")
        window.student_table.heading("studentimage",text="PhotoSample")
        window.student_table.heading("superviseid",text="superviseid")
        window.student_table["show"]="headings"
        
        window.student_table.column("studentid",width=150,anchor=CENTER)
        window.student_table.column("studentname",width=150,anchor=CENTER)
        window.student_table.column("studentyear",width=150,anchor=CENTER)
        window.student_table.column("studentgender",width=100,anchor=CENTER) 
        window.student_table.column("studendepartment",width=150,anchor=CENTER)      
        window.student_table.column("studentemail",width=220,anchor=CENTER)              
        window.student_table.column("studentphone",width=150,anchor=CENTER)        
        window.student_table.column("studentimage",width=150,anchor=CENTER)  
        window.student_table.column("superviseid",width=150,anchor=CENTER)  

        window.student_table.pack(fill=BOTH,expand=1)
        window.student_table.bind("<ButtonRelease>",window.get_cursor)
        window.fetch_data() 

    ## function decration 
    def add_data(self):
        global photo
        
        if self.var_dep.get()=="Select Department"  or self.var_std_id.get()=="" or photo is None:
            messagebox.showerror("Error","All Fields are required",parent=self.root)
              
        else:

            file_name_path = f"student/{self.var_std_id.get()}.png"
            cv2.imwrite(file_name_path, photo)
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="T12a34G56",database="face_recognizers")
                my_cursor=conn.cursor() 
                my_cursor.execute(f"insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                            self.var_std_id.get(),
                                                                                            self.var_name.get(),                                                                                            
                                                                                            self.var_year.get(),
                                                                                            self.var_gender.get(),  
                                                                                            self.var_dep.get(),                                                                                            
                                                                                            self.var_email.get(),                                                                                                                                                                             
                                                                                            self.var_phone.get(),
                                                                                            self.var_radio1.get(),
                                                                                            "80781"
                                                                                        ))
       
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #### Fetch  data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="T12a34G56",database="face_recognizers")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()       
        
        ### Get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_std_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_year.set(data[2]),
        self.var_gender.set(data[3]),
        self.var_dep.set(data[4]),
        self.var_phone.set(data[5]),
        self.var_email.set(data[6]),
        self.var_radio1.set(data[7])
        self.photo_label.config(image="")
        if data[8] != "":
            image_path = f"student/{data[0]}.png"
            image = Image.open(image_path)
            image = image.resize((440, 260), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.photo_label.config(image=photo)
            self.photo_label.image = photo
        else:
            self.photo_label.config(image="")
        
   
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department"  or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="T12a34G56",database="face_recognizers")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set studentname=%s,studentyear=%s,studentgender=%s,studendepartment=%s,studentemail=%s,studentphone=%s,studentimage=%s where studentid=%s",(
                     
                                                                                            
                                                                                            self.var_name.get(),                                                                                            
                                                                                            self.var_year.get(),
                                                                                            self.var_gender.get(),  
                                                                                            self.var_dep.get(),                                                                                            
                                                                                            self.var_email.get(),                                                                                                                                                                             
                                                                                            self.var_phone.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_std_id.get()        
                                                                                                )) 
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details succussfully updated",parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def update_data_photo(self):
        global photo
        if self.var_dep.get()=="Select Department"  or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            file_name_path = f"student/{self.var_std_id.get()}.png"            
            self.generate_dataset()
            
            os.remove(file_name_path)
            cv2.imwrite(file_name_path, photo)
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="T12a34G56",database="face_recognizers")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set studentname=%s,studentyear=%s,studentgender=%s,studendepartment=%s,studentemail=%s,studentphone=%s,studentimage=%s where studentid=%s",(
                     
                                                                                            
                                                                                            self.var_name.get(),                                                                                            
                                                                                            self.var_year.get(),
                                                                                            self.var_gender.get(),  
                                                                                            self.var_dep.get(),                                                                                            
                                                                                            self.var_email.get(),                                                                                                                                                                             
                                                                                            self.var_phone.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_std_id.get()        
                                                                                                )) 
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details succussfully updated",parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
                
    # Delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="T12a34G56",database="face_recognizers")
                    my_cursor=conn.cursor()
                    sq1="delete from exam_one_thirdper_second where studentid=%s"
                    sql="delete from student where studentid=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sq1,val)
                    my_cursor.execute(sql,val)
                    
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
                
    # Reset button
    def reset_data(self):
       
        self.var_std_id.set(""),
        self.var_name.set(""),       
        self.var_year.set("Select Year"),
        self.var_gender.set("Select Gender"),
        self.var_dep.set("Select Department"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")
    
    
    def generate_dataset(self):
            global photo
            try:
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.5, 2)
                    
                    for (x, y, w, h) in faces:
                        face_cropped_img = img[y:y+h, x:x+w]
                        return face_cropped_img

                cap = cv2.VideoCapture(0)
                img_id = 0
                
                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (440, 260))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        
                        cv2.imshow("Cropped face", face)
                        cv2.waitKey(1)
                        
                        key = cv2.waitKey(1) & 0xFF
                        if key == ord('q'):
                            pil_image = Image.fromarray(face)
                            resized_image = pil_image.resize((440, 260))

                        # Convert the resized image to a format that Tkinter can display
                            tk_image = ImageTk.PhotoImage(resized_image)

                        # Update the photo_label widget with the new image
                            self.photo_label.configure(image=tk_image)
                            self.photo_label.image = tk_image
                            photo = face
                            cap.release()
                            cv2.destroyAllWindows()
                            messagebox.showinfo("Result", "Generating datasets completed!")
                            break

                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    
                
                
if __name__ == "__main__":
    root=Tk() 
    obj=Student(root)
    root.mainloop()    