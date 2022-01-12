from tkinter import *
from tkinter import font
from main import *
from methods import *

# Colors
offWhite = "#FAF9F6"
btnColor = "#072227"
back = "#35838B"

def init(root):
    global frame
    frame = Frame(root).pack()
    welcome(root)

def welcome(root):
    cleanPage(root)
    box = Frame(root, bg = offWhite, width=800, height=400).pack(padx=100, pady=100)
    title = Label(root, text="Welcome to Flashcard App",font=("Roboto", 45), bg=offWhite).place(relx=.5, rely=.5, anchor=CENTER)
    startBtn = Button(root,text="START", padx=70, pady=20, font=("Roboto", 25), command=lambda:cardLib(root), border=0).place(relx=.5, rely=.845, anchor=CENTER)

def cardLib(root):
    cleanPage(root)
    box2 = Frame(root,width=800, height=400).pack(pady=100, side=BOTTOM)
    title = Label(root, text = "Card Library", font=('Roboto', 45), bg= back).place(relx=.5, rely=.1, anchor=CENTER)
    hint = Label(root, text="Click card deck to learn").place(relx=.5, rely=0.2, anchor=CENTER)
    createBtn = Button(root, text = "+ Create", command=lambda: createName(root), border=0,).place(relx=.8, rely=.1, anchor=CENTER)
    loadCards(box2)
    backBtn = Button(root, text = " < Back", command=lambda:welcome(root), border=0).place(relx=.2, rely=.1, anchor=CENTER)

def createName(root):
    cleanPage(root)
    namePrompt = Label(root, text="Please enter card's title: ", font=("Roboto", 40), bg=back).place(relx=.5, rely=.2, anchor=CENTER)
    global cardName
    cardName = StringVar()
    name = Entry(root, width=20, textvariable=cardName).place(relx=.5, rely=.3, anchor=CENTER)
    setBtn = Button(root, text = "Set Name", command=lambda: cardNaming(cardName, root), border=0).place(relx=.5, rely=.4, anchor=CENTER)
    openBtn = Button(root, text = "Open existing file", command=lambda:createWithFile(root), border=0).place(relx=.8, rely=.5, anchor=CENTER)
    backBtn = Button(root, text = " < Back", command=lambda:cardLib(root), border=0).place(relx=.2, rely=.1, anchor=CENTER)

def createCards(root):
    cleanPage(root)
    global word
    word = StringVar()
    global desc
    desc = StringVar()
    global cardName

    wordLbl = Label(root, text="Enter the word:", font=("Roboto", 30), bg=back).place(relx=.25, rely=.2, anchor=CENTER)
    wordInput = Entry(root, width=20, textvariable=word)
    wordInput.place(relx=.25, rely=.3, anchor=CENTER)
    descLbl = Label(root, text="Enter the description:", font=("Roboto", 30), bg=back).place(relx=.75, rely=.2, anchor=CENTER)
    descInput = Entry(root, width=20, textvariable=desc)
    descInput.place(relx=.75, rely=.3, anchor=CENTER)

    addBtn = Button(root, text = "+ add", command=lambda: addCard(word, desc, wordInput, descInput)).place(relx=.5, rely=.4, anchor=CENTER)
    doneBtn = Button(root, text = "Done creating", command=lambda: finishAdd(root)).place(relx=.8, rely=.6, anchor=CENTER)
    cancelBtn = Button(root, text = "Cancel", command=lambda: cancelCreate(root, cardName)).place(relx=.2, rely=.6, anchor=CENTER)

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

    cardDis = Button(root,textvariable=show, font=("Roboto",30),command = lambda: flip(show,list), height=10, width=30)
    cardDis.pack(pady=10)

    nextBtn = Button(root, text = "Next Word", command=lambda: nextWord(show,list))
    nextBtn.place(relx=.7, rely=.7, anchor=CENTER)

    backBtn = Button(root, text = "Previous Word", command=lambda: prevWord(show,list))
    backBtn.place(relx=.3, rely=.7, anchor=CENTER)

    finishBtn = Button(root, text = "Finish learning", command=lambda:cardLib(root))
    finishBtn.place(relx=.9, rely=.9, anchor=CENTER)
