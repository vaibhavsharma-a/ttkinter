from tkinter import *

root= Tk()
root.title("List boxes")
root.geometry("500x500")

#! create a frame for list box and scrollbar

listbox_scroller_frame = Frame(root)
my_scroller = Scrollbar(listbox_scroller_frame,orient=VERTICAL)

my_listbox = Listbox(listbox_scroller_frame,bd=5,width=50,yscrollcommand=my_scroller.set,selectmode=MULTIPLE)
my_scroller.config(command=my_listbox.yview)
my_scroller.pack(side=RIGHT,fill=Y)
listbox_scroller_frame.pack()
my_listbox.pack()

py_lis = ["put it in",23, 'gHjkL', 34.56, 78, 95.12, 'aBcDe', 12, 45.78, 'XyZzW', 89, 3.14, 'jKlMn', 67, 29.33, 'PqRst',"i get it","i lose","fuck man"]

for items in py_lis:
  my_listbox.insert(0,items)


get_put = Frame(root,bd=10,relief=RAISED)
get_put.pack(pady=7)
def put_in(var):
  pass
#! insert is the function to put the items in the list box, it takes the position and the item to be put in
  my_listbox.insert(END,var)
  item_entry.delete(0,END)


item_entry =  Entry(get_put,width=20,font=("Helevetica",15),bd=5,relief=GROOVE)
item_entry.pack(pady=10)

put_in_list_btn = Button(get_put,text="Put In!!",font=("Helevetica",8),bd=5,relief=RAISED,command =lambda: put_in(item_entry.get()))
put_in_list_btn.pack(pady=5)

#! deleteing items from the list

delt_frame = Frame(root,bd=3,relief=SUNKEN)
delt_frame.pack(pady=5)
#?delf function
def delt():
  my_listbox.delete(ANCHOR) # WHEN WE HIGHLIGHT SOMETHING IN THE LIST BY CLICLKING ON IT, IT BECOMES A ANCHOR
  selection_lable.config(text="")
#? delt button
delt_list_item_btn = Button(delt_frame,text="Delete it!",font=("Helevetica",8),bd=5,relief=RAISED,command=delt)
delt_list_item_btn.grid(row=0,column=0,pady=5)

#? delt all
def delt_everything():
  my_listbox.delete(0,END)
  selection_lable.config(text="")

def delt_everything_selected():
  
  for items in reversed(my_listbox.curselection()):
    my_listbox.delete(items)
  selection_lable.config(text="")


delt_all = Button(delt_frame,text="Delete All",font=("Helevetica",8),bd=5,relief=RAISED,command=delt_everything)
delt_all.grid(row=0,column=1,pady=5)

#? delete multiple selected on
del_mul_selected = Button(delt_frame,text="Delete Multiple selected",font=("Helevetica",8),bd=5,relief=RAISED,command=delt_everything_selected)
del_mul_selected.grid(row=1,column=0,columnspan=2,padx=5,pady=5)
#!selecting the item 


#? selection buttons frame

select_btn_frame = Frame(root,bd=3,relief=SUNKEN)
select_btn_frame.pack(pady=6)
#? select command

def select():

  selection_lable.config(text = my_listbox.get(ANCHOR))

def select_all():
  result = " "

  for items in my_listbox.curselection():
    result = result + str(my_listbox.get(items)) + "\n"

  selection_lable.config(text=result)

#? select button
select_buton = Button(select_btn_frame,text="select it!, show it",font=("Helevetica",8),bd=5,relief=RAISED,command=select)
select_buton.grid(row=0,column=0,padx=5)

#? select multiple
select_multiple_btn = Button(select_btn_frame,text="Select All",font=("Helevetica",8),bd=5,relief=RAISED,command=select_all)
select_multiple_btn.grid(row=0,column=1,padx=5)


#? selection lable
global selection_lable
selection_lable = Label(root,text="",font=("Helevetica",8))
selection_lable.pack(pady=5)

root.mainloop()