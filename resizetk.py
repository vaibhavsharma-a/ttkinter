import tkinter as tk
from PIL import Image, ImageTk

# Function to resize an image
def resize_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Initialize the main window
root = tk.Tk()
root.title("Image Resizing Example")

# Load and resize the image
image_path = "tkinter\\Nums\\1.png"  # Replace with your image path
new_size = (70, 90)  # Set the desired size (width, height)
resized_image = resize_image(image_path, new_size)

# Create a label and add the resized image
image_label = tk.Label(root, image=resized_image)
image_label.grid(row=0, column=0, padx=10, pady=10)

# Run the main event loop
root.mainloop()