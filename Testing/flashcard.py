from tkinter import *
 
root = Tk()

title = Label(text = "Flashcard").grid(row = 1, column=1)
 
input_text = Button(text="Text").grid(row = 3, column=0)
input_audio = Button(text="Audio").grid(row = 3, column=2)

root.mainloop()