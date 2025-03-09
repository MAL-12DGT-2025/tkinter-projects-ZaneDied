import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()

weapon = ["rock","paper","scissor"]
scoring = 0

def press(used):
    global scoring
    compWepn = random.randrange(0,3)
    if used != weapon[compWepn]:
        if (used == weapon[0] and compWepn == 2) or (used == weapon[1] and compWepn == 0) or (used == weapon[2] and compWepn == 1):
            scoring += 1
            score.config(text = str(scoring))
            result.config(text = f"You won!!, computer : {weapon[compWepn]}, chosen : {used}")
        else:
            result.config(text = f"Womp womp you lost!!, computer : {weapon[compWepn]}, chosen : {used}")
    else:
        result.config(text = f"keep trying buddy!!, computer : {weapon[compWepn]}, chosen : {used}")

root.title("RPS")
title = ttk.Label(root, text = "Rock Paper Scissors \n      Chose a item")
title.grid(row = 0 , column = 0, columnspan = 3, padx = 10, pady = 10,)

score = ttk.Label(root, text = "Score : 0")
score.grid(row = 1 , column = 0)

result = ttk.Label(root, text = "")
result.grid(row = 1, column = 1)

rockb = ttk.Button(root, text = "Rock", command = lambda : press("rock"))
rockb.grid(row = 2 , column = 0)

paperb = ttk.Button(root, text = "Paper", command = lambda : press("paper"))
paperb.grid(row = 2 , column = 1)

scissorb = ttk.Button(root, text = "Scissors", command = lambda : press("scissor"))
scissorb.grid(row = 2 , column = 2)


root.mainloop()

