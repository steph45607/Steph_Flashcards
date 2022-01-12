from tkinter import *

root = Tk()

box = Frame(root, width=100, height=100, bg="green").pack(side=TOP, padx=100)
with open("test.txt","r") as f:
    for row in f:
        row = row.strip("\n")
        row = Button(box, text = row).pack(side=TOP)

root.mainloop()