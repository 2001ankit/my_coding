import string
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
import time
import cv2
from uril import My_coding









# Note:import main project file
# from main_project import FaceRecognitionSystem


def main():
    win=Tk()
    app=Image_recognition(win)
    win.mainloop()

class Image_recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Image_recognition")
        self.root.geometry("1550x800+0+0")

        # self.bg=ImageTk.PhotoImage(file="images/SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img1 = Image.open("images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img1 = img1.resize((1530,800), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1530,height=800)

        title=Label(bg_lbl,text="All in one brand",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=120,width=1550,height=45)
        
        
        def time():
            string = strftime('%H:%M:%S %p')
            bg_lbl36.config(text = string)
            bg_lbl36.after(1000, time)
        bg_lbl36 = Label(bg_lbl,font = ('times new roman',14,'bold'),background = 'white',foreground = 'blue')
        bg_lbl36.place(x=5,y=120,width=120,height=40)
        time()
        
        
    
            

        # ==================== Project buttom(description) ==================================================
        # downtitle=Label(self.root,text="Note:Enter valid username and valid password",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="white",fg="blue")
        # downtitle.place(x=0,y=740,width=1600,height=35)

        myname=Label(self.root,text="Developed By:Ankit tripathi",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname.place(x=0,y=0)
        
        img10 = Image.open("images/facial-recognition_0.jpg")
        img10 = img10.resize((500,120), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1=Label(bg_lbl,image=self.photoImg10)
        bg_lbl1.place(x=0,y=0,width=500,height=120)

        img11 = Image.open("images/facialrecognition.png")
        img11 = img11.resize((500,120), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl22=Label(bg_lbl,image=self.photoImg11)
        bg_lbl22.place(x=500,y=0,width=500,height=120)

        img13 = Image.open("images/smart-attendance.jpg")
        img13 = img13.resize((550,120), Image.ANTIALIAS)
        self.photoImg13= ImageTk.PhotoImage(img13)
        bg_lbl12=Label(bg_lbl,image=self.photoImg13)
        bg_lbl12.place(x=1000,y=0,width=550,height=120)

        #student button
        img14 = Image.open("images/gettyimages-1022573162.jpg")
        img14 = img14.resize((380,350), Image.ANTIALIAS)
        self.photoImg14= ImageTk.PhotoImage(img14)

        b1=Button(bg_lbl,image=self.photoImg14,command=self.My_coding,cursor="hand2")
        b1.place(x=600,y=350,width=320,height=320)


        b1_1=Button(bg_lbl,text="No 1 Brand Site",command=self.My_coding,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="blue")
        b1_1.place(x=600,y=350,width=320,height=40)
        

        
        
    def My_coding(self):
        self.new_window=Toplevel(self.root)
        self.app=My_coding(self.new_window)
        
        
    
    
        
    

        
            

   
        

        

       



        

        
         

        
        
        

       


       

if __name__ == "__main__":
    main()
  