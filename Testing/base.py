from tkinter import *
# from PIL import ImageTk, Image

root = Tk() # First window
root.title("Making windows")

btn = Button(root, text ="Open second", command=lambda:open()).pack()

def open():
    top = Toplevel() # Second Window
    # To put things inside a specific window, assign the right variable as a window
    lable = Label(top, text="This is top").pack()


root.mainloop()