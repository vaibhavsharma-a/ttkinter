from tkinter import *
from PIL import ImageTk, Image


root = Tk()

Img1 = ImageTk.PhotoImage(Image.open(r"tkinter\images\img1.png"))
Img2 = ImageTk.PhotoImage(Image.open(r"tkinter\images\img2.png"))
Img3 = ImageTk.PhotoImage(Image.open(r"tkinter\images\img3.png"))
Img4 = ImageTk.PhotoImage(Image.open(r"tkinter\images\img4.png"))
Img5 = ImageTk.PhotoImage(Image.open(r"tkinter\images\img5.png"))
lab = Label(image=Img1)
lab.grid(row=0,column=0,columnspan=3)

button_fwd = Button(root,text=">>",padx=20,pady=10)
button_bck = Button(root,text="<<",padx=20,pady=10)
button_exit = Button(root,text="Exit", command=root.quit,padx=20,pady=10)

img_list = [Img1,Img2,Img3,Img4,Img5]


button_bck.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_fwd.grid(row=1,column=2)



root.mainloop()