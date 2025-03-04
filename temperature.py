import tkinter as tk

root = tk.Tk()


title = tk.Label(root,text = "Temperature\nconverter").grid(row = 0,column = 0)
number = tk.Entry(root).grid(row = 1, column = 0 )


ctofr = tk.Radiobutton(root, text = "Celsius to Fahrenheit").grid(row = 2, column = 0)
ftocr = tk.Radiobutton(root, text = "Fahrenheit to Celsius ").grid(row = 2, column = 1)

convb = tk.Button(root, text = "Convert").grid(row = 3, column = 0)
resl = tk.Label(root, text = "")

root.mainloop()