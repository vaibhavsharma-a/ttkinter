from tkinter import *



root = Tk()
root.title("Unicode Char")
root.geometry("400x400")

def unico_show():
  #! just get the number form the wikipedia and change it what unichar you want
  unicode = Label(root,text="41" + u'\u00b0' + "C",font=("Roman",20)).pack()
  unicode = Label(root,text="1000" + u'\u00a3' + " = 180,220" + u'\u00a5',font=("Roman",20)).pack()
  unicode = Label(root,text="T-Series" + u'\u00a9',font=("Roman",20)).pack()
  unicode = Label(root,text=u'\u2591',font=("Roman",20)).pack()
  unicode = Label(root,text=u'\u259a',font=("Roman",20)).pack()
  unicode = Label(root,text=u'\u2614',font=("Roman",20)).pack()

unicode_button = Button(root,text="Click to see Unicode chars",command=unico_show).pack(pady=10)
root.mainloop()