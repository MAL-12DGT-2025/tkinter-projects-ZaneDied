import tkinter as tk
from tkinter import ttk

def convertion(event):
    try:
        num = float(number.get())
        if rclick.get() == 1:
            #C to F
            result = (num * 9/5) + 32
            resl.config(text = f"{num}C is equal to {round(result,2)}F")


        elif rclick.get() == 2:
            #F to C
            result = (num - 32) * 5/9
            resl.config(text = f"{num}F is equal to {round(result,2)}C")
    except ValueError:
        resl.config(text="Not a valid number try again.")



root = tk.Tk()
root.title("Temperature Converter")
rclick = tk.IntVar(value = 1)


title = ttk.Label(root,text = "Temperature converter")
title.grid(row = 0,column = 0, columnspan=2, pady = 10, padx = 10)

number = tk.Entry(root)
number.grid(row = 1, column = 0,columnspan=2)



ctofr = ttk.Radiobutton(root, text = "Celsius to Fahrenheit", variable = rclick, value = 1)
ctofr.grid(row = 2, column = 0)

ftocr = ttk.Radiobutton(root, text = "Fahrenheit to Celsius ", variable = rclick, value = 2)
ftocr.grid(row = 2, column = 1)



convb = ttk.Button(root, text = "Convert", command = convertion)
convb.grid(row = 3, column = 0, columnspan=2)

resl = ttk.Label(root, text = "",)
resl.grid(row = 4, column= 0, columnspan=2)

root.bind("<Return>", convertion)

root.mainloop()