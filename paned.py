from tkinter import *

root = Tk()
root.title("Panned windows")
root.geometry("400x400")

pannel_1 = PanedWindow(bg="pink",bd=4,relief=SUNKEN)
pannel_1.pack(fill=BOTH,expand=1)

left_lab = Label(pannel_1,text="left lft")
pannel_1.add(left_lab)

left_bot = Label(pannel_1,text="Left Rgt")
pannel_1.add(left_bot)

#! panel number 2
pan_2 = PanedWindow(pannel_1,orient=VERTICAL,bg="green",bd=4,relief=SUNKEN)
pannel_1.add(pan_2)

#! adding stuff to panel 2
top = Label(pan_2,text="Top panel")
pan_2.add(top)

bottom = Label(pan_2,text="Bottom Pan")
pan_2.add(bottom)




root.mainloop()
