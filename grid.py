from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text ="Hello").grid(row=0, column=0)
myLabel2 = Label(root, text ="Meep").grid(row=1, column=0)


root.mainloop()