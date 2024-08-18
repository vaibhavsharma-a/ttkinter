from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Adding Frames in Tkinter")
root.iconbitmap("C:/Users/Asus/Downloads/marketing.ico")

frame = LabelFrame(root, text="This is a frame", padx=50,pady=50)
frame.pack(padx=10,pady=10)

button = Button(frame,text="Click me!")
button.grid(row=0,column=0)

button_2 = Button(frame,text="this is the second button")
button_2.grid(row=1,column=0)




root.mainloop()