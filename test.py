from tkinter import *
from PIL import *

root = Tk()

pic = PhotoImage(file = r"image/what.png")
btn = Button(root, image= pic, height=40, width=60).pack(side = TOP)

root.mainloop()