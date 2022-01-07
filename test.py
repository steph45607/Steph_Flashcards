from tkinter import *
from PIL import *

root = Tk()
root.config(bg = "blue")

pic = PhotoImage(file = r"image/createBtn.png")
btn = Button(root, image= pic, borderwidth=0)
btn.pack(side = TOP)


# def delete():
#     input.delete(0,END)

# input = Entry(root,width=20).pack()
# clear = Button(root, text = "clear", command=lambda: delete()).pack()


root.mainloop()
