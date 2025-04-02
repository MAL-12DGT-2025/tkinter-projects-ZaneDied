import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('900x500')

canvas = tk.Canvas(root,width=700,height=500)
canvas.grid(column=0, row=0)
canvas.create_oval(285,125,285+130,125+130,fill="#F8CECC",outline="#F8CECC")




size = (110, 110)
with Image.open("strawberry.png") as im:
    im.thumbnail(size)
    im.save("image_thumbnail.webp")

image = ImageTk.PhotoImage(im)
canvas.create_image(305,135,image = image)

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
