from tkinter import *
from main import *
from methods import *

def init(root):
    global frame
    frame = Frame(root).pack()
    welcome(root)

def welcome(root):
    cleanPage(root)
    title = Label(root, text="Welcome to Flashcard App", bg="lightgreen",font=("Roboto", 48)).place(relx=.5, rely=.4, anchor="c")
    start = Button(root, text = "Start", padx=70, pady=20, font=("Roboto", 25), command=lambda:cardLib(root)).place(relx=.5, rely=.55, anchor="c")

def cardLib(root):
    cleanPage(root)
    title = Label(root, text = "Card Library", font=('roboto', 30), bg="lightgreen").place(relx=.5, rely=.2, anchor="c")
    hint = Label(root, text="Click card deck to learn").pack()
    create = Button(root, text = "+ create card set", command=lambda: createName(root)).place(relx=.5, rely=.55, anchor="c")
    backButton = Button(root, text = " < Back", command=lambda:welcome(root)).pack()

def createName(root):
    cleanPage(root)
    namePrompt = Label(root, text="Please enter card's title: ").pack()
    global cardName
    cardName = StringVar()
    name = Entry(root, width=20, textvariable=cardName).pack()
    createButton = Button(root, text = "Create", command=lambda: cardNaming(cardName, root)).pack()
    openButton = Button(root, text = "Open existing file", command=lambda:createWithFile(root)).pack()
    backButton = Button(root, text = " < Back", command=lambda:cardLib(root)).pack()

def createCards(root):
    cleanPage(root)
    global word
    word = StringVar()

    global desc
    desc = StringVar()

    def delete():
        wordInput.delete(0,END)
        descInput.delete(0,END)
    wordLbl = Label(root, text="Enter the word:").pack()
    wordInput = Entry(root, width=20, textvariable=word).pack()
    descLbl = Label(root, text="Enter the description:").pack()
    descInput = Entry(root, width=20, textvariable=desc).pack()
    addButton = Button(root, text = "+ add", command=lambda: [addCard(word, desc), wordInput.delete(), descInput.delete()]).pack()
    doneButton = Button(root, text = "Done creating", command=lambda: finishAdd()).pack()
    cancelBtn = Button(root, text = "Cancel").pack()

def learnCards(root,list):
    cleanPage(root)
    global i
    i = 0
    cardDis = Button(root, text = list[i][0], command = lambda: flip(list))
    cardDis.pack()

    nextBtn = Button(root, text = "Next Word", command=lambda: nextWord(list))
    nextBtn.pack()

    backBtn = Button(root, text = "Previous Word", command=lambda: prevWord(list))
    backBtn.pack()

        

