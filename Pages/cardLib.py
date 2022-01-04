from tkinter import *
from tkinter import font

library = Tk()
library.title("Flashcard App")
library.geometry('1000x600')

title = Label(library, text = "Card Library", font=('roboto', 30), bg="lightgreen").pack()

create = Button(library, text = "+ create card set").pack()

mainloop()