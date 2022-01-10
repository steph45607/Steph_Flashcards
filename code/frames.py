from tkinter import *
from main import *
from methods import *

# Colors
offWhite = "#FAF9F6"
btnColor = "#072227"

def init(root):
    global frame
    frame = Frame(root).pack()
    welcome(root)

def welcome(root):
    cleanPage(root)
    inner = Frame(root, bg = offWhite, width=800, height=400).pack(padx=100, pady=100)
    title = Label(root, text="Welcome to Flashcard App",font=("Roboto", 45), bg=offWhite).place(relx=.5, rely=.5, anchor=CENTER)
    startBtn = Button(root,text="START", padx=70, pady=20, font=("Roboto", 25), command=lambda:cardLib(root), border=0).place(relx=.5, rely=.845, anchor=CENTER)

def cardLib(root):
    cleanPage(root)
    title = Label(root, text = "Card Library", font=('Roboto', 30), bg= offWhite).place(relx=.5, rely=.2, anchor=CENTER)
    hint = Label(root, text="Click card deck to learn").place(relx=.5, rely=0.3, anchor=CENTER)
    createBtn = Button(root, text = "+ create card set", command=lambda: createName(root), border=0,).place(relx=.5, rely=.55, anchor=CENTER)
    loadCards(root)
    backBtn = Button(root, text = " < Back", command=lambda:welcome(root), border=0).pack()

def createName(root):
    cleanPage(root)
    namePrompt = Label(root, text="Please enter card's title: ").pack()
    global cardName
    cardName = StringVar()
    name = Entry(root, width=20, textvariable=cardName).pack()
    setBtn = Button(root, text = "Set Name", command=lambda: cardNaming(cardName, root), border=0).pack()
    openBtn = Button(root, text = "Open existing file", command=lambda:createWithFile(root), border=0).pack()
    backBtn = Button(root, text = " < Back", command=lambda:cardLib(root), border=0).pack()

def createCards(root):
    cleanPage(root)
    global word
    word = StringVar()
    global desc
    desc = StringVar()
    global cardName

    wordLbl = Label(root, text="Enter the word:").pack()
    wordInput = Entry(root, width=20, textvariable=word)
    wordInput.pack()
    descLbl = Label(root, text="Enter the description:").pack()
    descInput = Entry(root, width=20, textvariable=desc)
    descInput.pack()
    addBtn = Button(root, text = "+ add", command=lambda: addCard(word, desc, wordInput, descInput)).pack()
    doneBtn = Button(root, text = "Done creating", command=lambda: finishAdd(root)).pack()
    cancelBtn = Button(root, text = "Cancel", command=lambda: cancelCreate(root, cardName)).pack()

def learnCards(root,list):
    cleanPage(root)

    global i
    i = 0

    show = StringVar()
    show.set(str(list[i][0]))

    def flip(show,list):
        """
        Method to flip card
        Manipulate button text
        """
        word = show.get()
        if word == str(list[i][0]):
            show.set(str(list[i][1]))
        else:
            show.set(str(list[i][0]))
    
    def nextWord(show,list):
        """
        Method to go to next word from list
        """
        global i
        if i == (len(list)-1):
            i = 0
            show.set(str(list[i][0]))
        else:
            i += 1
            show.set(str(list[i][0]))
    
    def prevWord(show,list):
        """
        Method to go to previous word from list
        """
        global i
        if i == 0:
            i = len(list)-1
            show.set(str(list[i][0]))
        else:
            i -= 1
            show.set(str(list[i][0]))

    cardDis = Button(root,textvariable=show, command = lambda: flip(show,list))
    cardDis.pack()

    nextBtn = Button(root, text = "Next Word", command=lambda: nextWord(show,list))
    nextBtn.pack()

    backBtn = Button(root, text = "Previous Word", command=lambda: prevWord(show,list))
    backBtn.pack()

    finishBtn = Button(root, text = "Finish learning", command=lambda:cardLib(root))
    finishBtn.pack()
