import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('700x500')

canvas = tk.Canvas(root,width=700,height=500)
canvas.grid(column=0, row=0)
canvas.create_oval(0,0,150,150,fill="#F8CECC",outline="#F8CECC")
canvas



size = (110, 110)
with Image.open("strawberry.png") as im:
    im.thumbnail(size)
    im.save("image_thumbnail.webp")

image = ImageTk.PhotoImage(im)
canvas.create_image(364,191,image = image)

"""image_label = tk.Label(root, image=image)
image_label.grid(row = 0, column = 0)
"""
def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        return px,py

root.bind('<Button-1>',onmouse)




root.mainloop()
