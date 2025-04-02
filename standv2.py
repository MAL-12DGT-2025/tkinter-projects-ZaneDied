import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('755x500')

size = (110, 110)
with Image.open("applle.png") as im:
    im.thumbnail(size)
    im.save("image_thumbnail.webp")

apple = ImageTk.PhotoImage(im)


appleimage = tk.Label(root, image=apple)
appleimage.grid(row = 0, column = 0)

with Image.open("lemonn.png") as i:
    i.thumbnail(size)
    i.save("image_thumbnail.webp")

lemon = ImageTk.PhotoImage(i)


lemonimage = tk.Label(root, image=lemon)
lemonimage.grid(row = 0, column = 1)



def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        return px,py

root.bind('<Button-1>',onmouse)




root.mainloop()
