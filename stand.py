import tkinter as tk 
from tkinter import ttk 


window = tk.Tk() 
window.geometry('350x400') 
window.title('Lemonade stand!!') 



ttk.Label(window, text = "Lemonade Stand", font = 15).grid(row = 0, column = 1) 


ttk.Label(window, text = "Select an item :").grid(column = 0, row = 5, padx = 10, pady = 25) 


op = tk.StringVar() 
menu = ttk.Combobox(window, width = 27, textvariable = op) 


menu['values'] = (
    
    "Lemonade drink $3",
    "Extra sugar 20% more",                         
    "Extra lemonade 10% more"                      
) 


menu.grid(column = 1, row = 5) 
menu.current() 
window.mainloop() 
