import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.geometry(f'{5*117}x500')

greattitle = ttk.Label(root, text = 'FRUIT MIX').grid(row = 0, column= 2)

def openimagec(namec,name):
    size = (110, 110)
    with Image.open(namec) as namec:
        namec.thumbnail(size)
        namec.save(f"{name}.webp")
        return ImageTk.PhotoImage(namec)

limec = openimagec("limec.png","limec")
limeimg = ttk.Label(root, image=limec).grid(row = 1, column = 0)

lemonc = openimagec("lemonc.png","lemonc")
lemonimg = ttk.Label(root, image=lemonc).grid(row = 1 , column = 1)

strawc = openimagec("strawc.png","strawc")
strawimg = ttk.Label(root, image=strawc).grid(row = 1 , column = 2)

orangec = openimagec("orangec.png","orangec")
orangeimg = ttk.Label(root, image=orangec).grid(row = 1 , column = 3)

applec = openimagec("applec.png","applec")
appleimg = ttk.Label(root, image=applec).grid(row = 1 , column = 4)








def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        return px,py

root.bind('<Button-1>',onmouse)




root.mainloop()
