import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
file_name = None

root = tk.Tk()
root.title("Python text editor")
root.minsize(width=400,height=400)
root.maxsize(width=1600,height=1600)

text = tk.Text(root)
text.pack()





def new_file():
  global file_name
  file_name = "Untitled"
  text.delete(0,tk.END)

def save_file():
  global file_name
  t = text.get("1.0",tk.END)
  f = open(file_name,'w')
  f.write(t)
  f.close()

def saveas_file():
  f = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
  t = text.get("1.0",tk.END)
  try:
    f.write(t.rstrip())
  except:
    messagebox.showerror(title="Opps",message="The file could not be saved...")

def open_file():
  f = filedialog.askopenfile(mode="r")
  t = f.read()
  text.delete("1.0",tk.END)
  text.insert("1.0", t)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New",command=new_file)
filemenu.add_command(label="Save As",command=saveas_file)
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Open File",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()