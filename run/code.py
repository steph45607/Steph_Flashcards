# Ask for input
# Use the input for the name of the deck
# name.txt
# add it to the list 
from tkinter import *
from frames import *
from main import *


global cardList
cardList = []

def cardNaming(n, frame):
    name = n.get()
    cardList.append(name)
    global root
    frames.createCards(frame)

def createDeck():
    pass

def cleanPage(root):
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration

def readFile():
    file = "example/english.txt"
    with open(file, "r") as f:

        # To split lines and assign to a list
        # With <word>\<word>
        match = []
        for i in f:
            match.append(i)
        # Remove \n from the end of the line
        match = map(lambda s: s.strip(), match)

        # To split every element inside the list by \
        # Assign it to a list
        words = [i.split("\\") for i in match]


        # Change to dictionary
        card = {}
        for i in range(len(words)):
            card[words[i][0]] = words[i][1]

        print(card)