from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")

def info():
  messagebox.showinfo("This is a popup", "Heal the world")

def warning():
  messagebox.showwarning("This is a warning","The world is about to end")

def error():
  messagebox.showerror("The Error","This the error in the thing")

def ques():
  responce = messagebox.askquestion("Question","You want to be a good guy?")
  # Label(root,text=responce).pack()
  if responce == "yes":
    Label(root,text="You will be a good guy soon").pack()
  else:
    Label(root,text="There is no scope of you being a good guy").pack()


def yesno():
  messagebox.askyesno("YES OR NO","This is the only world we have")
  

button = Button(root,text="Information",command=info).pack()
button = Button(root,text="Warning",command=warning).pack()
button = Button(root,text="Error",command=error).pack()
button = Button(root,text="Question",command=ques).pack()
button = Button(root,text="YES/NO",command=yesno).pack()




root.mainloop()