import tkinter as tk
from tkinter import ttk

root = tk.Tk()
rclick = tk.IntVar()

title = ttk.Label(root,text = "Temperature converter").grid(row = 0,column = 0, columnspan=2, pady = 10, padx = 10)
number = tk.Entry(root).grid(row = 1, column = 0,columnspan=2)


ctofr = ttk.Radiobutton(root, text = "Celsius to Fahrenheit", variable = rclick, value = 1).grid(row = 2, column = 0)
ftocr = ttk.Radiobutton(root, text = "Fahrenheit to Celsius ", variable = rclick, value = 2).grid(row = 2, column = 1)

convb = ttk.Button(root, text = "Convert").grid(row = 3, column = 0, columnspan=2)
resl = ttk.Label(root, text = "",).grid(row = 4, column= 0, columnspan=2)

root.mainloop()