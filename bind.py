from tkinter import *


root = Tk()
root.title("Bindings elements of tkinter")
root.geometry("400x400")

def binded(event):
  mylab = Label(root,text="The button is binded")
  mylab.pack()
  anothlab = Label(root,text="cordinates of the x and y " + str(event.x) + " " + str(event.y))
  anothlab.pack()

def keypress(event):
  keypreslab = Label(root,text=f"The key pressed is {event.char}")
  keypreslab.pack()


bindbutt = Button(root,text="Check binding")
bindbutt.bind("<Button-1>",binded)
bindbutt.pack()


keytyp = Button(root,text="Which key is pressed")
keytyp.bind("<Key>",keypress)
keytyp.pack()

root.mainloop()
