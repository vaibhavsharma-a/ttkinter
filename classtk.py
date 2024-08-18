from tkinter import *

root = Tk()
root.title("Using classes")
root.geometry("400x400")


class put:
  def __init__(self,master):
    myFrame = Frame(master)
    myFrame.pack()

    

    self.mybutton = Button(master,text="Clicker")
    self.mybutton.bind("<Key>",self.click)
    self.mybutton.pack(pady=20)

  def click(self,event):
    self.mylab = Label(master=root,text="clicked the button" + str(event.x) + " " + str(event.y))
    
    self.mylab.pack()
    self.charlab = Label(master=root,text=f'you have clicked {event.char} key on the keyboard')
    self.charlab.pack()

    

r = put(root)
root.mainloop()

    
    