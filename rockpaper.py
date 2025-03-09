import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()

weapon = ["rock","paper","scissor"]
def press(used):
    compWepn = random.randrange(0,3)
    print(weapon[compWepn])
    print(used, 2)
    playerWepn = used
    if playerWepn != weapon[compWepn]:
        if playerWepn == weapon[0] and compWepn == 2:
            title.config(text = f"YOU WOONN!!, computer : {weapon[compWepn]}, you : {used}")
        elif playerWepn == weapon[1] and compWepn == 0:
            title.config(text = f"YOU WOONN!!, computer : {weapon[compWepn]}, you : {used}")
        elif playerWepn == weapon[2] and compWepn == 1:
            title.config(text = f"YOU WOONN!!, computer : {weapon[compWepn]}, you : {used}")
        else:
            title.config(text = f"Womp womp you lost!!, computer : {weapon[compWepn]}, you : {used}")
    else:
        title.config(text = f"keep trying buddy!!, computer : {weapon[compWepn]}, you : {used}")

root.title("RPS")
title = ttk.Label(root, text = "Rock Paper Scissors \n chose")
title.grid(row = 0 , column = 0, columnspan = 5, padx = 10, pady = 10,)

rockb = ttk.Button(root, text = "Rock", command = lambda : press("rock"))
rockb.grid(row = 1 , column = 0)

paperb = ttk.Button(root, text = "Paper", command = lambda : press("paper"))
paperb.grid(row = 1 , column = 1)

scissorb = ttk.Button(root, text = "Scissors", command = lambda : press("scissor"))
scissorb.grid(row = 1 , column = 2)


root.mainloop()

