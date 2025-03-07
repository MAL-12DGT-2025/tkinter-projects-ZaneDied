import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

lineq = ""
results = ""


def press(val):
    global lineq
    global results
    try:
        if val == "=" or val == "\r":
            total = str(eval(lineq))
            result.config(text=total)
            lineq = total
            results = total
        elif val == "c":
            lineq = ""
            results = ""
            result.config(text="0")
        else:
            numer = str(val)
            if numer.isnumeric() or numer == ".":
                lineq = lineq + str(val)
                results = results + str(val)
            else:
                lineq = lineq + str(val)
                if val == "*":
                    results = f"{results} x "
                else:
                    results = f"{results} {val} "

            result.config(text=results)
    except SyntaxError:
        lineq = ""
        results = ""
        result.config(text="Error")


def keyprs(event):
    num = event.char
    if num.isnumeric(
    ) or num == "/" or num == "*" or num == "+" or num == "-" or num == "c" or num == "\r" or num == "=":
        press(num)
    else:
        pass


result = ttk.Label(root, text="0")
result.grid(
    row=0,
    column=0,
    columnspan=5,
    padx=10,
    pady=10,
)

btn7 = ttk.Button(root, text="7", command=lambda: press(7))
btn7.grid(row=1, column=1)

btn8 = ttk.Button(root, text="8", command=lambda: press(8))
btn8.grid(
    row=1,
    column=2,
)

btn9 = ttk.Button(root, text="9", command=lambda: press(9))
btn9.grid(row=1, column=3)

btndev = ttk.Button(root, text="/", command=lambda: press("/"))
btndev.grid(row=1, column=4)

btn4 = ttk.Button(root, text="4", command=lambda: press(4))
btn4.grid(row=2, column=1)

btn5 = ttk.Button(root, text="5", command=lambda: press(5))
btn5.grid(row=2, column=2)

btn6 = ttk.Button(root, text="6", command=lambda: press(6))
btn6.grid(row=2, column=3)

btnx = ttk.Button(root, text="x", command=lambda: press("*"))
btnx.grid(row=2, column=4)

btn1 = ttk.Button(root, text="1", command=lambda: press(1))
btn1.grid(row=3, column=1)

btn2 = ttk.Button(root, text="2", command=lambda: press(2))
btn2.grid(row=3, column=2)

btn3 = ttk.Button(root, text="3", command=lambda: press(3))
btn3.grid(row=3, column=3)

btnmin = ttk.Button(root, text="-", command=lambda: press("-"))
btnmin.grid(row=3, column=4)

btnc = ttk.Button(root, text="C", command=lambda: press("c"))
btnc.grid(row=4, column=1)

btn0 = ttk.Button(root, text="0", command=lambda: press(0))
btn0.grid(row=4, column=2)

btndot = ttk.Button(root, text=".", command=lambda: press("."))
btndot.grid(row=4, column=3)

btnpls = ttk.Button(root, text="+", command=lambda: press("+"))
btnpls.grid(row=4, column=4)

btneq = ttk.Button(root, text="=", command=lambda: press("="))
btneq.grid(row=5, column=1, columnspan=5, ipadx=115)

root.bind('<Key>', keyprs)

root.mainloop()
