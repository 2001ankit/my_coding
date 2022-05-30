#Open google in python - Windows
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import random
import time
import webbrowser

def main():
    win=Tk()
    app=My_coding(win)
    win.mainloop()

class My_coding:
    def __init__(self,root):
        self.root=root
        self.root.title("Image_recognition")
        self.root.geometry("1550x800+0+0")
        url='https://amazon.com'
        webbrowser.get('"C:\Program Files\Google\Chrome\Application\chrome.exe" %s').open(url)

if __name__ == "__main__":
    main()
