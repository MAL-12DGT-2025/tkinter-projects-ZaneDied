import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

lineq = ""

def press(val):
    global lineq
    lineq = lineq + str(val)
    lineq.set()

def eqpress():

    try:

        global lineq
        total = str(eval(lineq))
        result.config(text = total)
        lineq = ""
    except:
        result.config(text = "ERROR")
        print(lineq)


result = ttk.Label(root, text = "Null")
result.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10, )

btn7 = ttk.Button(root, text = "7", command= lambda : press(7))
btn7.grid(row = 1 , column = 1)

btn8 = ttk.Button(root, text = "8")
btn8.grid(row = 1 , column = 2)

btn9 = ttk.Button(root, text = "9")
btn9.grid(row = 1, column = 3)

btndev = ttk.Button(root, text = "/")
btndev.grid(row = 1, column = 4)


btn4 = ttk.Button(root, text = "4")
btn4.grid(row = 2, column = 1)

btn5 = ttk.Button(root, text = "5")
btn5.grid(row = 2, column = 2)

btn6 = ttk.Button(root, text = "6")
btn6.grid(row = 2, column = 3)

btnx = ttk.Button(root, text = "x")
btnx.grid(row = 2, column = 4)


btn1 = ttk.Button(root, text = "1")
btn1.grid(row = 3, column = 1)

btn2 = ttk.Button(root, text = "2")
btn2.grid(row = 3, column = 2)

btn3 = ttk.Button(root, text = "3")
btn3.grid(row = 3, column = 3)

btnmin = ttk.Button(root, text = "-")
btnmin.grid(row = 3, column = 4)


btnc = ttk.Button(root, text = "C")
btnc.grid(row = 4, column = 1)

btn0 = ttk.Button(root, text = "0")
btn0.grid(row = 4, column = 2)

btndot = ttk.Button(root, text = ".")
btndot.grid(row = 4, column = 3)

btnpls = ttk.Button(root, text = "+")
btnpls.grid(row = 4, column = 4)

btneq = ttk.Button(root, text = "=")
btneq.grid(row = 5, column = 1, columnspan = 5, ipadx = 115)




root.mainloop()
