from tkinter import *
from tkinter import filedialog, messagebox
import os
from ast import *

from frames import *
from main import *
from factory import *

"""
Temporary list, easier to append
from user input
"""
global cards
cards = []


def cardNaming(n, frame):
    """
    Function to create
    deck name from user input
    """
    # Get the name from Entry input
    name = n.get()
    
    # Won't allow user to create a card with empty name
    if name == "":
        error = messagebox.showerror(title="Card Naming", message="Name can't be empty")
    else:
        # Write the name into a cardlist file to store it
        with open("storage/cardlist.txt", "a") as f:
            f.write(name + "\n")
        # Call to run the createCards frame
        frames.createCards(frame)


def createWithFile(frame):
    """
    Method to create card deck
    from user's existing file
    """
    # Get file from path
    file = filedialog.askopenfilename(initialdir="/", title="Select existing file", filetypes=[("Text Files", "*.txt")])
    
    if file == "":
        # If the user cancel to add file, it will go back to the window and add nothing to the storage
        frames.createName(frame)
    else:
        # Call to run readFile method
        readFile(file, frame)


def addCard(front, back, wordInput, descInput):
    """
    Method to add one card to the list
    from user input and file
    """
    global cards

    # Access global list and append value from user input to list
    cards.append([front.get(), back.get()])
    
    # Clean the entry box
    deleteEntry(wordInput, descInput)


def deleteEntry(word, desc):
    """
    Method to clear the entry user input
    in card making page after user add a pair
    """
    word.delete(0,END)
    desc.delete(0,END)


def finishAdd(frame):
    """
    Method to signal program that the user
    finsih adding cards to deck
    Will store list to cardStorage
    """
    with open("storage/cardStorage.txt", "a") as f:
        global cards
        # Write list to cardStorage file, change type to string
        f.write(str(cards)+"\n")
    
    # Assign empty list to cards, ready to use to make another deck
    cards = []

    # Return user to card libarary page
    frames.cardLib(frame)


def deleteName(n):
    """
    Method to delete deck name from cardlist file
    """
    name = n.get()+"\n"
    with open("storage/cardlist.txt","r") as f:
        titles = f.readlines()
    with open("storage/cardlist.txt","w") as f:
        for title in titles:
            if title != name:
                f.write(title)


def cancelCreate(frame, name):
    """
    Method to delete a created deck of cards
    """ 
    deleteName(name)
    cards = []
    frames.cardLib(frame)


def readFile(file, frame):
    """
    Method to read user's file
    """
    # Add the file name to cardlist file as card's deck name
    with open("storage/cardlist.txt", "a") as f:
        f.write(os.path.splitext(os.path.basename(file))[0]+"\n")

    # Open the user file and change to list
    with open(file, "r") as f:
        global words
        words = []
        for i in f:
            i = i.replace("\n", "")
            words.append(i)
    
        for i in range(len(words)):
            words[i] = words[i].split("\\")
    
    # Add the list to cardStorage file
    with open("storage/cardStorage.txt", "a") as f:
        f.write(str(words)+"\n")

    # Will let the user to learn the cards once they add the file
    frames.learnCards(frame, words)


def loadCards(frame, frame2):
    """
    Method to load the cards in card library page
    """
    # List to store objects
    buttons = []
    # Open file of card list and storage
    with open("storage/cardlist.txt") as lst, open("storage/cardstorage.txt") as strg:
        # Access to read the lines
        name = lst.readlines()
        words = strg.readlines()
        # Iterate through the file per line
        for i in range(len(name)):
            # Use ast to make a string of list to a list
            words[i] = literal_eval(words[i])
            # Object creation
            button = Deck(frame, name[i], words[i])
            # Append object to buttons list
            buttons.append(button)
    # Iterate through the buttons object list to create button
    for btn in buttons:
        # Use method from class to create button
        btn.buttonMake(frame2, btn.getName(), btn.getList())
 
          
def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration
