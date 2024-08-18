from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("The root Window")
lab = Label(root, text="this is in the root window").pack()

def open():
  global my_image
  top = Toplevel()
  top.title("Top level window")
  lable = Label(top,text="this is in the top level window").pack()
  my_image = ImageTk.PhotoImage(Image.open(r"tkinter/images/img1.png"))
  lable = Label(top,image=my_image).pack()
  btn2 = Button(top,text="close second window",command=top.destroy).pack()

button = Button(root,text="Click to open window",command=open).pack()



root.mainloop()