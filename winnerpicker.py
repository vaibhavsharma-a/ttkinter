from tkinter import *
from random import randint


root = Tk()
root.title("Pick winner")
root.geometry("400x400")
root.configure(bg="Grey")

def pick_win():
  
  # wins = Tk()
  # wins.title("This show the winners")
  # wins.geometry("400x400")
  prop_win_list = [
    "SkyWalker92", "PixelMaster", "NeonTiger1", "EchoNight", "BlazePhoenix", 
    "VortexWolf", "CrimsonFalcon", "AquaKnight", "CyberNinja", "MysticShadow", 
    "StormRider", "GamerGhost", "QuantumFlux", "SilentHunter", "IronDragon", 
    "ShadowBlaze", "NinjaStrike", "Frostbite", "ThunderHawk", "LunarEclipse", 
    "StealthWraith", "Hypernova", "OmegaKnight", "GalacticWarrior", "DarkRaven", 
    "SolarFlare", "RogueAgent", "PhantomRider", "FireFury", "AbyssWalker", 
    "DigitalSorcerer", "ZenithDragon", "ViperStrike", "CyberKnight", "ShadowSphinx", 
    "IronWarlord", "BlazeKnight", "NeoSpartan", "QuantumNinja", "SilentPhantom", 
    "StormShadow", "GamerWolf", "MysticTiger", "CrimsonViper", "AquaSorcerer", 
    "NeonPhoenix", "SkyRider", "EchoDragon", "VortexKnight", "PixelPhantom", 
    "BlazeWraith", "ThunderRider", "LunarWarrior", "CyberSorcerer", "MysticRaven", 
    "SilentViper", "StormKnight", "EchoPhoenix", "GamerKnight", "QuantumWarlord"
  ]
  global labs
  labs = []
  number = int(num.get())
  for _ in range(0,number):
     
    random_number = randint(0,len(prop_win_list)-1)
  
    global on_screen
    on_screen = Label(root,text=prop_win_list[random_number],foreground="#B7950B",font=("Courier",30))
    on_screen.pack()
    labs.append(on_screen)

  pick.config(state=DISABLED)
  
  


winner = Label(root,text="Pick-O-Winner",foreground="#2ECC71",font=("Times",30))
winner.pack()

want = Label(root,text="Enter the number of winner you want to draw").pack(pady=2)


num = Entry(root,width=20,border=4)
num.pack(pady=5)

pick =  Button(root,text="Pick winner",command=pick_win,width=20,height=3,foreground="Blue",bg="lightpink",relief="groove")
pick.pack()

def clear():
    for lables in labs:
      lables.destroy()
    labs.clear()
    num.delete(0,END)
    pick.config(state=NORMAL)

rst = Button(root,text="RESET",command=clear,fg="#20DBF1",bg="#A60000",relief="ridge",padx=10).pack(padx=10,pady=10)

tooltip = Label(root, text="Use Reset to Enable", bg="red")

def show_tooltip(event):
    if pick["state"] == DISABLED:
      x, y, _, _ = pick.bbox("insert")
      x += pick.winfo_rootx() - pick.winfo_x()
      y += pick.winfo_rooty() - pick.winfo_y()
      tooltip.place(x=x, y=y)

def hide_tooltip(event):
    tooltip.place_forget()

pick.bind("<Enter>", show_tooltip)
pick.bind("<Leave>", hide_tooltip)


root.mainloop()