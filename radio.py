from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("lear about radio buttons")

bat = StringVar()
bat.set("")

types = [
  ("G.M","Gunn&Moore"),
  ("MRF","MRF"),
  ("Kukkarbura","Kukkabura"),
  ("Grey Nicoles","Grey Nicoles")
]

def clicked(value):
  mylable = Label(root,text=value)
  mylable.pack()

for text, type in types:
  Radiobutton(root,text=text,variable=bat,value=type).pack(anchor=W)

button = Button(root, text="Bat Brand",command=lambda:clicked(bat.get()))
button.pack(anchor=W)


root.mainloop()