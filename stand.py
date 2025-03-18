import tkinter as tk 
from tkinter import ttk 


root = tk.Tk() 
root.geometry('400x400') 
root.title('Lemonade stand!!') 
constal = {

    "Lemonade drink $3":"3",
    "Sprite Lemonade $5":"5",
    "Ice tea $4":"4",     

}
cartv = ""
carv = ""
def press(ops):
    global carv
    global cartv
    menop = menu.get()
    if ops == "add":
        cartv =  f"{menop} + {cartv} "
        carv =  str(eval(cartv))
        cart.config(text = f"{cartv} = {carv}")


ttk.Label(root, text = "Lemonade Stand").grid(row = 0, column = 1) 
ttk.Label(root, text = "Select an item :").grid(row = 1, column = 0,  padx = 10, pady = 25) 
cart = ttk.Label(root, text = "Cart: ")
cart.grid(row = 5, column = 1)

menu = ttk.Combobox(root, width = 27)
menu.grid(row = 1 , column = 1)

extra = ttk.Combobox(root, width = 27)
extra.grid_remove()

extra['values'] = (

    "Extra sugar +$20%",                         
    "Extra lemon +$10%",
    "Medium cup +$30%",
    "Large cup +$60%",             

)

menu['values'] = (
    
    "Lemonade drink $3",
    "Sprite Lemonade $5",
    "Ice tea $4"     

) 


addb = ttk.Button(root, text = "Add", command = lambda : press("add"))
addb.grid(row = 2, column = 0)

removeb = ttk.Button(root, text = "Remove", command = lambda : press("remove"))
removeb.grid(row = 3 , column = 0 )

checkoutb = ttk.Button(root, text =  "Checkout", command = lambda : press("checkout"))
checkoutb.grid(row = 4 , column = 0)

menu.current(0) 
root.mainloop() 
