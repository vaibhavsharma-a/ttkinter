from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Runs scored by a player")
root.iconbitmap(r"C:\Users\Asus\Downloads\52740cricketgame_109412.ico")
root.geometry("200x200")

def graph():
  scored = np.random.normal(100,10,5)
  plt.polar(scored)
  plt.show()
  
graph_button = Button(root,text="Plot the graph",command=graph).pack()




root.mainloop()