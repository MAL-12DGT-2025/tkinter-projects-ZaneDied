import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.geometry("666x500")

greattitle = ttk.Label(root, text = 'FRUIT MIX').grid(row = 0, column= 2)

padix = 10
padbx = 20

def openimagec(namec,name):
    size = (110, 110)
    with Image.open(namec) as namec:
        namec.thumbnail(size)
        namec.save(f"{name}.webp")
        return ImageTk.PhotoImage(namec)

limec = openimagec("limec.png","limec")
limeimg = ttk.Label(root, image=limec).grid(row = 2, column = 0, padx=padix)

lemonc = openimagec("lemonc.png","lemonc")
lemonimg = ttk.Label(root, image=lemonc).grid(row = 2, column = 1, padx=padix)

strawc = openimagec("strawc.png","strawc")
strawimg = ttk.Label(root, image=strawc).grid(row = 2, column = 2, padx=padix)

orangec = openimagec("orangec.png","orangec")
orangeimg = ttk.Label(root, image=orangec).grid(row = 2, column = 3, padx=padix)

applec = openimagec("applec.png","applec")
appleimg = ttk.Label(root, image=applec).grid(row = 2, column = 4, padx=padix)

style = ttk.Style()
hovercol = "deepskyblue"
unhovercol = "skyblue"
style.configure("addb.TButton", background=unhovercol)
style.map("addb.TButton",background=[("active",hovercol)])

add1 = ttk.Button(root,text = "Add",style='addb.TButton')
add1.grid(row = 3, column = 0, padx = padbx)

add2 = ttk.Button(root, text = "Add", style = 'addb.TButton')
add2.grid(row = 3, column = 1, padx=padbx)

add3 = ttk.Button(root, text = "Add", style = 'addb.TButton')
add3.grid(row = 3, column = 2, padx=padbx)

add4 = ttk.Button(root, text = "Add", style ='addb.TButton')
add4.grid(row = 3, column = 3, padx=padbx)

add5 = ttk.Button(root, text = "Add",style = 'addb.TButton')
add5.grid(row = 3, column = 4, padx=padbx)


def onmouse(event):
        px = []
        py = []
        px.append(event.x)
        py.append(event.y)
        print(px , py)
        print(root.winfo_reqheight(), root.winfo_reqwidth())

root.bind('<Button-1>',onmouse)


root.mainloop()
