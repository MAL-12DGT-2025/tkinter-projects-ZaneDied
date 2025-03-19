
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry('400x400')
root.title('Lemonade stand!!')
dictcost = {
    "Lemonade drink $3": "3",
    "Sprite Lemonade $5": "5",
    "Ice tea $4": "4",
}
cart_items = []
total = 0

def press(ops):
    global total
    if ops == "add":
        cart_items.append(menu.get())
        total += float(dictcost[menu.get()])
        cart.config(text=f"Cart: {' + '.join(cart_items)}\nTotal: ${total:.2f}")

    elif cart_items or menu.get() in cart_items:
        if ops == "checkout":
            
            messagebox.showinfo("Checkout", f"Total amount: ${total:.2f}\nThank you for your purchase!")
            cart_items.clear()
            total = 0
            cart.config(text="Cart: ")

        elif ops == "remove":
            try:
                cart_items.remove(menu.get())
                total -= float(dictcost[menu.get()])
                cart.config(text=f"Cart: {' + '.join(cart_items)}\nTotal: ${total:.2f}")
            except ValueError:
                messagebox.showwarning("Cart ERROR", f"{menu.get()} : Not in the cart")

    else:
        messagebox.showwarning("Cart ERROR", "Nothing in the cart")


ttk.Label(root, text="Lemonade Stand").grid(row=0, column=1)
ttk.Label(root, text="Select an item :").grid(row=1,column=0,padx=10,pady=25)
cart = ttk.Label(root, text="Cart: ")
cart.grid(row=5, column=1)

menu = ttk.Combobox(root, width=27)
menu.grid(row=1, column=1)


menul = (
    "Lemonade drink $3",
    "Sprite Lemonade $5", 
    "Ice tea $4",
)


menu['values'] = menul

addb = ttk.Button(root, text="Add", command=lambda: press("add"))
addb.grid(row=2, column=0)

addeb = ttk.Button(root, text = "Add", command = lambda: press("adde"))
addeb.grid_remove()

removeb = ttk.Button(root, text="Remove", command=lambda: press("remove"))
removeb.grid(row=3, column=0)

checkoutb = ttk.Button(root,text="Checkout",command=lambda: press("checkout"))
checkoutb.grid(row=4, column=0)

menu.current(0)
root.mainloop()
