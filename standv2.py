import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()

size = (100, 150)
with Image.open("strawberry.png") as im:
    im.thumbnail(size)
    im.save("image_thumbnail.webp")

image = ImageTk.PhotoImage(im)
image_label = tk.Label(root, image=image)
image_label.grid(row = 1, column = 0)


root.mainloop()
