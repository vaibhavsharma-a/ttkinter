from tkinter import *


root = Tk()
root.title("Menues")
root.geometry("400x400")

def dothing():
  pass
menu_my = Menu(root)
root.configure(menu=menu_my)

def file_frame():
  del_all_frames()
  new_file_frame.pack(fill=BOTH,expand=1)
  file_lab = Label(root,text="You have clicked File >> New")
  file_lab.pack()

def edit_frame():
  del_all_frames()
  new_edit_frame.pack(fill=BOTH,expand=1)
  edit_lab = Label(root,text="You have clicked Edit >> Undo")
  edit_lab.pack()

def del_all_frames():
  for widget in new_edit_frame.winfo_children():
    widget.destroy()
    
  for widge in new_file_frame.winfo_children():
    widge.destroy()

  new_file_frame.forget()
  new_edit_frame.forget()
  


#! file menu
file_menu = Menu(menu_my)
menu_my.add_cascade(label= "File",menu=file_menu)

file_menu.add_command(label="New...",command=file_frame)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#! Edit menu
edit_menu = Menu(menu_my)
menu_my.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo",command=edit_frame)
edit_menu.add_command(label="Redo",command=dothing)
edit_menu.add_command(label="Cut",command=dothing)
edit_menu.add_command(label="Copy",command=dothing)
edit_menu.add_command(label="Select All",command=dothing)

#! Option Menu
option_menu = Menu(menu_my)
menu_my.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Find",command=dothing)
option_menu.add_command(label="Find All",command=dothing)
option_menu.add_command(label="Go To",command=dothing)


#! new file frame
new_file_frame = Frame(root,width=400,height=400,bg="Lightpink")

#! new edit frame
new_edit_frame = Frame(root,width=400,height=400,bg="Skyblue")

root.mainloop()
