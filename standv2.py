import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('900x600')

canvas = tk.Canvas(root,width=520,height=300)
canvas.grid(column=0, row=0)
canvas.create_oval(0,0,150,150,fill="red")



size = (100, 150)
with Image.open("strawberry.png") as im:
    im.thumbnail(size)
    im.save("image_thumbnail.webp")

image = ImageTk.PhotoImage(im)
image_label = tk.Label(root, image=image)
image_label.grid(row = 0, column = 0)






root.mainloop()
