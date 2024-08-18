from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning icons and images")
root.iconbitmap("C:/Users/Asus/Downloads/marketing.ico")


#exit button
button_quit = Button(root,text="exit from this program", command=root.quit)

button_quit.pack()

my_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Asus\Pictures\Screenshots\Screenshot 2024-03-30 211138.png"))
my_lable = Label(image=my_image)
my_lable.pack()


root.mainloop()