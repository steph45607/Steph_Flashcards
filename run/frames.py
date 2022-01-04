from tkinter import *
from main import *
from code import cardNaming, cleanPage

def init(root):
    global frame
    frame = Frame(root).pack()
    welcome(root)

def welcome(root):
    title = Label(root, text="Welcome to Flashcard App", bg="lightgreen",font=("Roboto", 48)).place(relx=.5, rely=.4, anchor="c")
    start = Button(root, text = "Start", padx=70, pady=20, font=("Roboto", 25), command=lambda:cardLib(root)).place(relx=.5, rely=.55, anchor="c")

def cardLib(root):
    cleanPage(root)
    title = Label(root, text = "Card Library", font=('roboto', 30), bg="lightgreen").place(relx=.5, rely=.2, anchor="c")
    create = Button(root, text = "+ create card set", command=lambda: createName(root)).place(relx=.5, rely=.55, anchor="c")

def createName(root):
    cleanPage(root)
    namePrompt = Label(root, text="Please enter card's title: ").pack()
    global cardName
    cardName = StringVar()
    name = Entry(root, width=20, textvariable=cardName).pack()
    createButton = Button(root, text = "Create", command=lambda: cardNaming(cardName, root)).pack()

def createCards(root):
    cleanPage(root)
    word = Label(root, text="Enter the word:").pack()
    wordInput = Entry(root, width = 20).pack()
    desc = Label(root, text="Enter the description:").pack()
    descInput = Entry(root, width=20).pack()
    addButton = Button(root, text = "+ add").pack()

    


    
# root = Tk()
# welcome(root)
# root.mainloop()