from tkinter import *

root = Tk()

with open("test.txt","r") as f:
    for row in f:
        row = row.strip("\n")
        row = Button(root, text = row).pack()

root.mainloop()