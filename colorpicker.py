from tkinter import *
from tkinter import colorchooser


root = Tk()
root.title("COLOR PICKER")
root.geometry("400x400")

def pick_color():
  #? colorchooser returns a python list at 0 index it has a dict of different RBG values and at index 1 we have hexcodes of color selected

  # my_colr = colorchooser.askcolor()[0][2] #! trying to get the third value from RBG dict

  # on_Screen = Label(root,text=f"{my_colr:.0f}").pack(pady=20)

  my_Colr = colorchooser.askcolor()[1]
  
  text_on_Screen = Label(root,text="You have picked this color",fg=my_Colr,font=("Roman",15)).pack(pady=8)

  def hexcode():
    hex_Code = Label(root,text=my_Colr).pack(pady=5)


  reveal = Button(root,text="Reveal Hexcode",relief=RAISED,command=hexcode)
  reveal.pack(pady=5)




btn = Button(root,text="Choose a color",bg="pink",bd=5,relief=RAISED,command=pick_color)
btn.pack()

root.mainloop()