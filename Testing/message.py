from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox # to have message box

root = Tk()
root.title('Mesage Box')

def popup():
    messagebox.askquestion("A popup", "This is the message") # to show the text inside the box
    # showwarning
    # showerror

    # ask keywords can store value to a variable if messagebox.ask- is assigned to a variable
    # askquestion - yes 1 no 0
    # askokcancel - ok 1 cancel 0
    # askyesno - yes yes no no

Button(root, text='popup', command=popup).pack()




root.mainloop()