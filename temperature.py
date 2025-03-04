import tkinter as tk

root = tk.Tk()


title = tk.Label(root,text = "Temperature\nconverter").grid(row = 0,column = 0)
number = tk.Entry(root).row(row = 1, column = 0 )

root.mainloop()