from tkinter import *
from PIL import ImageTk, Image
import pymysql

root = Tk()
root.title("CRM database")
root.iconbitmap(r"C:\Users\Asus\Downloads\HomeServer_icon-icons.com_55232.ico")
root.geometry("300x300")

mydb = pymysql.connect(
  host = "localhost",
  user = "root",
  passwd = "password123",
  database = "None" 
)

print(mydb)

root.mainloop()