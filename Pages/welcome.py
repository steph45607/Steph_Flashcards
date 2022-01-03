from tkinter import *
from tkinter import font

welcome = Tk()
welcome.title("FlashCard App")

welcome.geometry("1000x600")

title = Label(welcome, text="Welcome to Flashcard App", bg="lightgreen",font=("Roboto", 48)).place(relx=.5, rely=.4, anchor="c")
start = Button(welcome, text = "Start", padx=70, pady=20, font=("Roboto", 25)).place(relx=.5, rely=.55, anchor="c")

mainloop()