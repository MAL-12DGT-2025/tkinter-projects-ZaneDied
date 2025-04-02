import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('755x500')
size = (110, 110)



with Image.open("limee.png") as limepng:
     limepng.thumbnail(size)
     limepng.save("limepng.webp")

limeimage = ImageTk.PhotoImage(limepng)


limepng = tk.Label(root, image=limeimage)
limepng.grid(row = 0, column = 0)





def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        return px,py

root.bind('<Button-1>',onmouse)




root.mainloop()
