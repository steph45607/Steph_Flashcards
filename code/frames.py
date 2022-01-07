from tkinter import *
from main import *
from methods import *

# Colors
offWhite = "#FAF9F6"
btnColor = "#072227"

# Button images
#imgStart = Image.open("image/startBtn.png")
#imgStart = ImageTk.PhotoImage(((Image.open("image/startBtn.png")).resize(50,100)))

def init(root):
    global frame
    frame = Frame(root).pack()
    welcome(root)

def welcome(root):
    cleanPage(root)
    inner = Frame(root, bg = offWhite, width=800, height=400).pack(padx=100, pady=100)
    title = Label(root, text="Welcome to Flashcard App", bg=offWhite,font=("Roboto", 45)).place(relx=.5, rely=.5, anchor="c")
    startBtn = Button(root,text="START", padx=70, pady=20, font=("Roboto", 25), command=lambda:cardLib(root), border=0, fg = "white",bg=btnColor).place(relx=.5, rely=.845, anchor="c")

def cardLib(root):
    cleanPage(root)
    title = Label(root, text = "Card Library", font=('roboto', 30), bg=offWhite, ).place(relx=.5, rely=.2, anchor="c")
    hint = Label(root, text="Click card deck to learn").pack()
    createBtn = Button(root, text = "+ create card set", command=lambda: createName(root), border=0, fg = "white",bg=btnColor).place(relx=.5, rely=.55, anchor="c")
    backBtn = Button(root, text = " < Back", command=lambda:welcome(root), border=0, fg = "white",bg=btnColor).pack()

def createName(root):
    cleanPage(root)
    namePrompt = Label(root, text="Please enter card's title: ").pack()
    global cardName
    cardName = StringVar()
    name = Entry(root, width=20, textvariable=cardName).pack()
    setBtn = Button(root, text = "Set Name", command=lambda: cardNaming(cardName, root), border=0, fg = "white",bg=btnColor).pack()
    openBtn = Button(root, text = "Open existing file", command=lambda:createWithFile(root), border=0, fg = "white",bg=btnColor).pack()
    backBtn = Button(root, text = " < Back", command=lambda:cardLib(root), border=0, fg = "white",bg=btnColor).pack()

def createCards(root):
    cleanPage(root)
    global word
    word = StringVar()
    global desc
    desc = StringVar()

    wordLbl = Label(root, text="Enter the word:").pack()
    wordInput = Entry(root, width=20, textvariable=word)
    wordInput.pack()
    descLbl = Label(root, text="Enter the description:").pack()
    descInput = Entry(root, width=20, textvariable=desc)
    descInput.pack()
    addBtn = Button(root, text = "+ add", command=lambda: addCard(word, desc, wordInput, descInput)).pack()
    doneBtn = Button(root, text = "Done creating", command=lambda: finishAdd(root)).pack()
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
