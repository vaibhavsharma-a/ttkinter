from tkinter import *

root = Tk()
root.title("Drop down box")
root.geometry("400x400")

checked = StringVar()
checked.set("Select the type of blowing")

options = ["Fast",
           "Off-spin",
           "Medium-Pace",
           "Leg spin"]

def reset():
  checked.set("Select the type of bowling")

def show():
  mylabe = Label(root,text=checked.get()).pack()

drop = OptionMenu(root,checked,*options)
drop.pack()

rst = Button(root,text="reset",command=reset).pack()
showing = Button(root,text="Show selectio",command=show).pack()
root.mainloop()