from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title("Flashacard!")
root.geometry("600x600")
root.iconbitmap(r"C:\Users\Asus\Downloads\geography_822.ico")


def randomize():
  
  our_States = ['andhra pradesh','arunachal pradesh','assam','goa','bihar','chhattisgarh','gujarat','haryana','himachal pradesh','karnataka','madhya pradesh','maharashtra','punjab','rajasthan']

  rndo = randint(0,len(our_States)-1)
  global ans_state 
  ans_state = our_States[rndo]
  # state = "tkinter\\states\\" + our_States[rndo] + ".gif" 

  global show_sts
  show_sts = ImageTk.PhotoImage(Image.open("tkinter\\states\\" + our_States[rndo] + ".gif"))
  lab.config(image=show_sts)

def state_cap_answere():
  if capital_radi.get() == our_capitals[ans.title()]:
    resp = "Correct " + our_capitals[ans.title()] + " is the Capital of " + ans.title()
  else:
    resp = "Wrong " + our_capitals[ans.title()] + " is the Capital of " + ans.title()

  state_cap_lable.config(text=resp)

def addition_randomizer():
  global num_1,num_2
  num_1 = randint(0,10)
  num_2 = randint(0,10)

  #! creating lables to be put on the pic_frame
  # num_1_lab = Label(pic_frame)
  # num_2_lab = Label(pic_frame)
  # addition_sign = Label(pic_frame,text="+",font=("Helvetica",20))

  # Function to resize an image
  def resize_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


  global image_num_1
  global image_num_2

  select_card_1 = resize_image("tkinter\\Nums\\" + str(num_1) + ".png",(200,200))
  select_card_2 = resize_image("tkinter\\Nums\\" + str(num_2) + ".png",(200,200))


  image_num_1 = select_card_1
  image_num_2 = select_card_2
  #!putting them on screen with gird system
  num_1_lab.grid(row=0,column=0)
  addition_sign.grid(row=0,column=1)
  num_2_lab.grid(row=0,column=2)

  #! config the lables
  num_1_lab.config(image=image_num_1)
  num_2_lab.config(image=image_num_2)

#! checking and showing addition answer
def check_ans():
  total = int(num_1) + int(num_2)
  if int(addition_ans_entry.get()) == total:
    respon = "Correct, " + str(num_1) + " + " + str(num_2) + " = " + str(total)
  else:
    respon = "Check your answer " + str(num_1) + " + " + str(num_2) + " = " + str(total) + ", NOT " + addition_ans_entry.get()
  addition_check_lab.config(text=respon)

  addition_ans_entry.delete(0,END)
  addition_randomizer()

  
  
  
#! for addition flascard
def addi():
  hide_all_frames()

  add_frame.pack(fill=BOTH,expand=1)

  add_lable = Label(add_frame,text="Addition Flashcard", font=("Helvetica",15)).pack(pady=5)
  pic_frame = Frame(add_frame, width=400,height=300)
  pic_frame.pack()

  global num_1,num_2
  num_1 = randint(0,10)
  num_2 = randint(0,10)

  #! creating lables to be put on the pic_frame
  global num_1_lab,num_2_lab,addition_sign
  num_1_lab = Label(pic_frame)
  num_2_lab = Label(pic_frame)
  addition_sign = Label(pic_frame,text="+",font=("Helvetica",20))

  # Function to resize an image
  def resize_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


  global image_num_1
  global image_num_2

  select_card_1 = resize_image("tkinter\\Nums\\" + str(num_1) + ".png",(200,200))
  select_card_2 = resize_image("tkinter\\Nums\\" + str(num_2) + ".png",(200,200))


  image_num_1 = select_card_1
  image_num_2 = select_card_2
  #!putting them on screen with gird system
  num_1_lab.grid(row=0,column=0)
  addition_sign.grid(row=0,column=1)
  num_2_lab.grid(row=0,column=2)

  #! config the lables
  num_1_lab.config(image=image_num_1)
  num_2_lab.config(image=image_num_2)


  #! answere box
  global addition_ans_entry
  addition_ans_entry = Entry(add_frame,width=20,font=("Helvetica",20),bd=5,relief=SUNKEN)
  addition_ans_entry.pack(pady=10)

  #! answere button
  addition_ans_btn = Button(add_frame,text="Check Answere",font=("Helvetica",10),bd=3,relief=RAISED,command=check_ans)
  addition_ans_btn.pack(pady=10)

  #! answer correct/wrong lab
  global addition_check_lab
  addition_check_lab = Label(add_frame,text="",font=("Helvetica",15))
  addition_check_lab.pack()





def display_ans():
  if ans_entr.get().lower() == ans_state:
    ans_lab.config(text="Your answer is correct" + u'\u2713' + " , it is " + ans_state.title())
  else:
    ans_lab.config(text="Your answer is wrong" + u'\u274c' + " , it is " + ans_state.title())
  randomize()
  ans_entr.delete(0, END)

def Show_states():
  hide_all_frames()
  states_frame.pack(fill=BOTH,expand=1)
  # state_lb = Label(states_frame,text="Will be showing states ⏳.... " + u'\u27f3')
  # state_lb.pack()
  '''
  our_States = ['andhra pradesh','arunachal pradesh','assam','goa','bihar','chhattisgarh','gujrat','haryana','himachal pradesh','karnataka','madhya pradesh','maharashtra','punjab','rajasthan']

  rndo = randint(0,len(our_States)-1)
  global ans_state 
  ans_state = our_States[rndo]
  # state = "tkinter\\states\\" + our_States[rndo] + ".gif" 

  global show_sts
  show_sts = ImageTk.PhotoImage(Image.open("tkinter\\states\\" + our_States[rndo] + ".gif"))
  '''
  global lab
  lab = Label(states_frame)
  lab.pack(pady=5)
  randomize()

  #create next button to go to next states
  next_but = Button(states_frame,text="Pass, Idk",bd=4,relief=RAISED,command=Show_states)
  next_but.pack(pady=5)

  # get answers
  global ans_entr
  ans_entr = Entry(states_frame,width=30,font=("Helvetica,20"),border=4,bg="#dff9f4")
  ans_entr.pack(pady=5)

  # finalizing answer button
  # global ans_button
  ans_button = Button(states_frame, text="Answer",bd=5,relief=RIDGE,command=display_ans)
  ans_button.pack(pady=5)

  # answer lable
  global ans_lab
  ans_lab = Label(states_frame,text="",font=("Helvetica",18))
  ans_lab.pack(pady=5)

def Show_states_cap():
  hide_all_frames()
  states_Cap_frame.pack(fill=BOTH,expand=1)
  # state_cap_lb = Label(states_Cap_frame,text="Will be showing state's capital ⏳ ....." + u'\u27f3')
  # state_cap_lb.pack()
  global lab
  lab = Label(states_Cap_frame)
  lab.pack(pady=5)

  

  global our_States
  our_States = ['andhra pradesh','arunachal pradesh','assam','goa','bihar','chhattisgarh','gujarat','haryana','himachal pradesh','karnataka','madhya pradesh','maharashtra','punjab','rajasthan']

  global our_capitals
  our_capitals = {
      "Andhra Pradesh": "Amaravati",
      "Arunachal Pradesh": "Itanagar",
      "Assam": "Dispur",
      "Bihar": "Patna",
      "Chhattisgarh": "Raipur",
      "Goa": "Panaji",
      "Gujarat": "Gandhinagar",
      "Haryana": "Chandigarh",
      "Himachal Pradesh": "Shimla",
      "Karnataka": "Bengaluru",
      "Madhya Pradesh": "Bhopal",
      "Maharashtra": "Mumbai",
      "Punjab": "Chandigarh",
      "Rajasthan": "Jaipur",
  }

  #! doing all the above thing in one loop
  ans_list = []
  cnt = 1
  global ans
  while cnt < 4:
      rnd = random.randint(0,len(our_States)-1)
      if cnt ==1:
          #? if the cnt is one that is first time then consider it as our ans for the state
          ans = our_States[rnd]
          global show_sts_cap
          show_sts_cap = ImageTk.PhotoImage(Image.open("tkinter\\states\\" + ans + ".gif"))
          lab.config(image=show_sts_cap)

      
      #? put that to the ans_list
      ans_list.append(our_States[rnd])

      #? remove the selected one from the main state list
      our_States.remove(our_States[rnd])

      #? shuffle the rest to get more randomization
      random.shuffle(our_States)

      cnt +=1
    
  global capital_radi
  capital_radi = StringVar()
  capital_radi.set("None")

  capital_radi_1 = Radiobutton(states_Cap_frame,text=our_capitals[ans_list[0].title()],variable = capital_radi,value=our_capitals[ans_list[0].title()], font=("Helvetica",15))
  capital_radi_1.pack()
  capital_radi_2 = Radiobutton(states_Cap_frame,text=our_capitals[ans_list[1].title()],variable = capital_radi,value=our_capitals[ans_list[1].title()], font=("Helvetica",15))
  capital_radi_2.pack()
  capital_radi_3 = Radiobutton(states_Cap_frame,text=our_capitals[ans_list[2].title()],variable = capital_radi,value=our_capitals[ans_list[2].title()],font=("Helvetica",15))
  capital_radi_3.pack()

  pass_but = Button(states_Cap_frame,text="Pass, Idk",bd=4,relief=RAISED,command=Show_states_cap)
  pass_but.pack(pady=5)

  state_cap_button = Button(states_Cap_frame,text="Confirm Answer!",bd=5,relief=RIDGE, command=state_cap_answere)
  state_cap_button.pack(pady=5)

  global state_cap_lable
  state_cap_lable = Label(states_Cap_frame, text="", font=("Helvetica",15))
  state_cap_lable.pack(pady=5)

  pass_but = Button(states_Cap_frame,text="Next",bd=4,relief=GROOVE,command=Show_states_cap,bg="red",fg="white")
  pass_but.pack(pady=5)


def hide_all_frames():
  for widget in states_frame.winfo_children():
    widget.destroy()

  for wid in states_Cap_frame.winfo_children():
    wid.destroy()

  for widge in add_frame.winfo_children():
    widge.destroy()

  states_frame.pack_forget()
  states_Cap_frame.pack_forget()
  add_frame.pack_forget()

my_mnu = Menu(root)
root.configure(menu=my_mnu)

#! geography menu
states = Menu(my_mnu)
my_mnu.add_cascade(label="Geography",menu=states)
states.add_command(label="States",command=Show_states)
states.add_command(label="States Capital",command=Show_states_cap)
states.add_separator()
states.add_command(label="Exit",command=root.quit)

#! creating maths menu
Maths_mnu = Menu(my_mnu)
my_mnu.add_cascade(label="Maths",menu=Maths_mnu)
Maths_mnu.add_command(label="Addition",command=addi)

#! making frames for these menu
states_frame = Frame(root,width=500,height=500)
states_Cap_frame = Frame(root,width=500,height=500)

#! making frames for the addition flashcard

add_frame = Frame(root,height=500,width=500)

root.mainloop()

