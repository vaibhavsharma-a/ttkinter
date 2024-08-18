from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Check box")

var = StringVar()

def show():
  mylable = Label(root,text=var.get()).pack()

check = Checkbutton(root,text="Check if you are 18+",variable=var,onvalue="18+",offvalue="Underage")
check.deselect()
check.pack()

button = Button(root,text="Show check box status",command=show).pack()



root.mainloop()