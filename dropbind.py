from tkinter import *
from tkinter import ttk

root = Tk()
root.title("dropdown binding")
root.geometry("400x400")





options = [
  "Batsman",
  "Bowler",
  "Wicket-keeper",
  "Allrouder",
  "Coach",
  "Team Manager",
  "Fielder",
]


vari = StringVar()
vari.set("Choose a Role")

def chose(event):
  mylab = Label(root,text=vari.get())
  mylab.pack()
  if vari.get() == "Batsman":
    mylab = Label(root,text="I hope you become one like kohli")
    mylab.pack()
  elif vari.get() == "Bowler":
    mylab = Label(root,text="Practice and be like boom boom!")
    mylab.pack()
    
def comboselected(event):
  mylab = Label(root,text=combo.get())
  mylab.pack()
  


drop = OptionMenu(root,vari,*options,command=chose)
drop.pack()

combo = ttk.Combobox(root,values=options)
combo.current("0")
combo.pack()
combo.bind("<<ComboboxSelected>>",comboselected)

# seleted = Button(root,text="Role Choosen",command=chose)
# seleted.pack()

root.mainloop()