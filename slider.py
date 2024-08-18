from tkinter import *

root = Tk()
root.title("Differe sliders")
root.geometry("400x400")
veritcal = Scale(root, from_=50,to=700)
veritcal.pack(anchor=W)

horizon = Scale(root, from_=50, to= 700,orient=HORIZONTAL)
horizon.pack(anchor=W)

def sliderh():
  my_lable = Label(root,text=horizon.get()).pack()
  root.geometry(str(horizon.get()) + "x400")

def sliderv():
  my_lable = Label(root,text=veritcal.get()).pack()
  root.geometry("400x" + str(veritcal.get()))


button = Button(root,text="set Horizontal dimention",command=sliderh).pack()
button = Button(root,text="set vertical dimention",command=sliderv).pack()
root.mainloop()