import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("File reader")
count = 0
fileexplore = ""
def fsearch(chc,op):
        files = os.listdir()
        listf = ""
        for file in files:
            if file.endswith(".txt"):
                listf = f"{file.rsplit('.', maxsplit=1)[0]}\n{listf}"  
        if listf == "":
                listf = "No files found"
        elif chc == "get":
            print(listf)
            return listf
        elif chc == "check":
            if op in listf:
                return True
            else:
                 return False
        return listf
def bpress(ty):
    global count
    global fileexplore
    if ty == "search":
        count = 0
        returnl.config(text = fsearch("get",None))
    if ty == "read":
        count = 0
        try:
            f = open(f"{direc.get()}.txt", "r", encoding = 'utf-8')
            returnl.config(text = f.read())
        except Exception as e:
            returnl.config(text=f"{type(e).__name__}")
    if ty == "write":
        if count == 0:
              if fsearch("get",None) != "No files found":
                direc.set("")
                returnl.config(text = f"Chose a file to edit and then press\n write again to start writing. \n{fsearch("get",None)}")
                count += 1
              else:
                   direc.set("No files found.")
        elif count == 1:
            fileexplore = direc.get()
            if fsearch("check",fileexplore):
                direc.set("")
                returnl.config(text = "Start typing to append into file \n once finish press write agian.")
                count += 1
            else:
                 returnl.config(text = "No file found.")
        elif count == 2:
            f = open(f"{fileexplore}.txt","w")
            f.write(direc.get())
            f.close()
            count = 0
            direc.set("")
            returnl.config(text = "Finished")

    
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