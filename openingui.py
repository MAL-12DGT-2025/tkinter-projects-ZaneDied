import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("File reader")

def bpress(ty):
    if ty == "search":
        files = os.listdir()
        listf = ""
        for file in files:
            if file.endswith(".txt"):
                listf = f"{file}\n{listf}" 
        listf = listf.rstrip(listf[-4:])
        returnl.config(text = listf)
        
    if ty == "read":
        try:
            f = open(f"{direc.get()}.txt", "r")
            returnl.config(text = f.read())
        except Exception as e:
            returnl.config(text=f"{type(e).__name__}")
            
    
direc = tk.StringVar()
entryn = ttk.Entry(root, textvariable = direc)
entryn.grid(row = 2, column = 1)

header = ttk.Label(root, text = "Python text reader \npress search to start")
header.grid(row = 0, column = 1)

readb = ttk.Button(root, text = "Read", command = lambda : bpress("read"))
readb.grid(row = 1, column = 0)

writeb = ttk.Button(root, text = "Write", command = lambda : bpress("write"))
writeb.grid(row = 1, column = 1)

searchb = ttk.Button(root, text = "Search", command = lambda : bpress("search"))
searchb.grid(row = 1, column = 2)

returnl = ttk.Label(root, text = "")
returnl.grid(row = 3, column = 1)






root.mainloop()