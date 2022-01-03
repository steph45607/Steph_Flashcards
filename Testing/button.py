from tkinter import *

root = Tk()

# Creating buttons
# third parameter for button, state
# Can be equal to DISABELED --> to disable the button, cant be clicked

# padx = change size of x axis
# pady = change size of y axis

# Create function to make the button do something
def myClick():
    myLabel = Label(root, text="Button clicked").pack()

myButton = Button(root, text="Click this", command=myClick, fg="red").pack()

root.mainloop()