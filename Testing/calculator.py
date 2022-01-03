from tkinter import *

root = Tk()
root.title("Calculator") # Set the name of the window / tab

input = Entry(root, width=20) # To make an empty input field, change width with keyword
input.grid(row = 0,column=0,columnspan=3)

def button_num(num):
    # input.delete(0,END)
    current = input.get()
    input.delete(0,END)
    input.insert(0, str(current) + str(num))

def button_clear():
    input.delete(0,END)

def button_add():
    first = input.get()
    global fnum
    global math
    math = "add"
    fnum = first
    input.delete(0,END)

def button_sub():
    first = input.get()
    global fnum
    global math
    math = "sub"
    fnum = first
    input.delete(0,END)

def button_multiply():
    first = input.get()
    global fnum
    global math
    math = "multiply"
    fnum = first
    input.delete(0,END)

def button_div():
    first = input.get()
    global fnum
    global math
    math = "div"
    fnum = first
    input.delete(0,END)

def button_equal():
    second = input.get()
    input.delete(0,END)

    if math == "add":
        input.insert(0,int(fnum) + int(second))
    elif math == "sub":
        input.insert(0,int(fnum) - int(second))
    elif math == "multiply":
        input.insert(0,int(fnum) * int(second))
    elif math == "div":
        input.insert(0,int(fnum) / int(second))

one = Button(root, text = "1", padx=40, pady = 20, command=lambda: button_num(1)).grid(row=3, column=0)
two = Button(root, text = "2", padx=40, pady = 20, command=lambda: button_num(2)).grid(row=3, column=1)
three = Button(root, text = "3",  padx=40, pady = 20, command=lambda: button_num(3)).grid(row=3, column=2)

four = Button(root, text = "4",  padx=40, pady = 20, command=lambda: button_num(4)).grid(row=2, column=0)
five = Button(root, text = "5",  padx=40, pady = 20, command=lambda: button_num(5)).grid(row=2, column=1)
six = Button(root, text = "6",  padx=40, pady = 20, command=lambda: button_num(6)).grid(row=2, column=2)

seven = Button(root, text = "7",  padx=40, pady = 20, command=lambda: button_num(7)).grid(row=1, column=0)
eight = Button(root, text = "8",  padx=40, pady = 20, command=lambda: button_num(8)).grid(row=1, column=1)
nine = Button(root, text = "9",  padx=40, pady = 20, command=lambda: button_num(9)).grid(row=1, column=2)

zero = Button(root, text = "0",  padx=40, pady = 20, command=lambda: button_num(0)).grid(row=4, column=0)
clear = Button(root, text = "clear",  padx=90, pady = 20, command = lambda: button_clear()).grid(row=4, column=1, columnspan=2)

add = Button(root, text = "+",  padx=40, pady = 20, command=lambda: button_add()).grid(row=5, column=0)
sub = Button(root, text = "-",  padx=40, pady = 20, command=lambda: button_sub()).grid(row=6, column=0)
multiply = Button(root, text = "x",  padx=40, pady = 20, command=lambda: button_multiply()).grid(row=6, column=1)
divide = Button(root, text = "/",  padx=40, pady = 20, command=lambda: button_div()).grid(row=6, column=2)
equal = Button(root, text = "=",  padx=100, pady = 20, command=lambda: button_equal()).grid(row=5, column=1, columnspan=2)

root.mainloop()