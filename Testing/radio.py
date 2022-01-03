from tkinter import *


root = Tk()
root.title("Making radio things")

# r = IntVar() # to make the variable to be integer based
# # StrVar - for string
# r.set("2")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text = text, variable=pizza, value=topping).pack(anchor=W)

def click(value):
    myLabel = Label(root, text= value)
    myLabel.pack()


# Radiobutton(root, text = "option 1", variable = r, value = 1,command=lambda: click(r.get())).pack() # Will make the variable r to 1
# Radiobutton(root, text = "option 2", variable = r, value = 2, command = lambda: click(r.get())).pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button (root, text = "Click this", command=lambda: click(pizza.get()))
myButton.pack()

root.mainloop()