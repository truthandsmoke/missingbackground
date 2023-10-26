import os
import time
from PIL import Image, ImageTk
import tkinter as tk

# Directory containing your images
image_dir = "C:/path/to/your/images"

# Get a list of image file names in the directory
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".png", ".gif", ".bmp"))]

if not image_files:
    print("No image files found in the directory.")
    exit()

# Initialize the tkinter window
root = tk.Tk()
root.title("Image Slideshow")
root.geometry("800x600")  # Set your preferred window size

# Create a label to display the images
image_label = tk.Label(root)
image_label.pack(fill=tk.BOTH, expand=True)

# Function to update the displayed image
def update_image():
    global current_image, photo
    if current_image >= len(image_files):
        current_image = 0

    img = Image.open(os.path.join(image_dir, image_files[current_image]))
    img = img.resize((root.winfo_width(), root.winfo_height()), Image.ANTIALIAS)  # Resize the image to fit the window
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

    current_image += 1
    root.after(15000, update_image)  # Update the image every 15 seconds

current_image = 0
update_image()
root.mainloop()
