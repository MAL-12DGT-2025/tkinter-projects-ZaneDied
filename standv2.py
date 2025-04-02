import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.geometry('755x500')
size = (110, 110)
oranges = (118,118)

greattitle = ttk.Label(root, text = 'THE GREAT FRUIT').grid(row = 0, column= 2)

def openimagec(namec,size):
    with Image.open(namec) as namec:
        namec.thumbnail(size)
        namec.save("limepng.webp")
        return ImageTk.PhotoImage(namec)

limec = openimagec("limec.png",size)
limeimg = ttk.Label(root, image=limec).grid(row = 1, column = 0,padx=10)

lemonc = openimagec("lemonc.png",size)
lemonimg = ttk.Label(root, image=lemonc).grid(row = 1 , column = 1,padx=10)

strawc = openimagec("strawc.png",size)
strawimg = ttk.Label(root, image=strawc).grid(row = 1 , column = 2,padx=10)

orangec = openimagec("orangec.png",oranges)
orangeimg = ttk.Label(root, image=orangec).grid(row = 1 , column = 3,padx=10)

applec = openimagec("applec.png",size)
appleimg = ttk.Label(root, image=applec).grid(row = 1 , column = 4,padx=10)








def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        return px,py

root.bind('<Button-1>',onmouse)




root.mainloop()
