from tkinter import *

root = Tk()
root.title("Calculator")

input = Entry(root, width=20)
input.grid(row = 0,column=0,columnspan=3)

def button_add(num):
    return

one = Button(root, text = "1", command=lambda: button_add(1)).grid(row=3, column=0)
two = Button(root, text = "2", command=lambda: button_add(2)).grid(row=3, column=1)
three = Button(root, text = "3", command=lambda: button_add(3)).grid(row=3, column=2)

four = Button(root, text = "4", command=lambda: button_add(4)).grid(row=2, column=0)
five = Button(root, text = "5", command=lambda: button_add(5)).grid(row=2, column=1)
six = Button(root, text = "6", command=lambda: button_add(6)).grid(row=2, column=2)

seven = Button(root, text = "7", command=lambda: button_add(7)).grid(row=1, column=0)
eight = Button(root, text = "8", command=lambda: button_add(8)).grid(row=1, column=1)
nine = Button(root, text = "9", command=lambda: button_add(9)).grid(row=1, column=2)

zero = Button(root, text = "0", command=lambda: button_add(0)).grid(row=4, column=0)
clear = Button(root, text = "clear").grid(row=4, column=1, columnspan=2)

add = Button(root, text = "+").grid(row=5, column=0)
equal = Button(root, text = "=").grid(row=5, column=1, columnspan=2)

root.mainloop()