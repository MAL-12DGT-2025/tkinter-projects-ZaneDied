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
image_label.pack()


with Image.open("apple.png") as ime:
    ime.thumbnail(size)
    ime.save("image_apple.webp")

imeg= ImageTk.PhotoImage(ime)
imeg_label = tk.Label(root, image=imeg)
imeg_label.pack()
root.mainloop()
