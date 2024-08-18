from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Accessing Files")

def open():
  global my_image
  root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Asus\Desktop\pyproj\tkinter\images",title="select files",filetypes=(("png files","*.png"),("All files","*.*")))
  my_image = ImageTk.PhotoImage(Image.open(root.filename))
  image_lable = Label(root,image=my_image).pack()

# leb = Label(root,text=root.filename).pack()

button = Button(root,text="Open file",command=open).pack()
button = Button(root,text="Quit",command=root.quit).pack()
root.mainloop()