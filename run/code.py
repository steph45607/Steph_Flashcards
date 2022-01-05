from tkinter import *
from frames import *
from main import *
from tkinter import filedialog
import os

global cardList

def cardNaming(n, frame):
    name = n.get()

    with open("storage/cardlist.txt", "a") as f:
        f.write(name + "\n")

    global root
    frames.createCards(frame)

def createWithFile(frame):
    file = filedialog.askopenfilename(initialdir="/", title="Select existing file")
    readFile(file, frame)

def cleanPage(root):
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration

def readFile(file, frame):
    with open("storage/cardlist.txt", "a") as f:
        f.write(os.path.splitext(os.path.basename(file))[0]+"\n")

    with open(file, "r") as f:
        global words
        words = []
        for i in f:
            i = i.replace("\n", "")
            words.append(i)
    
        for i in range(len(words)):
            words[i] = words[i].split("\\")

       
        frames.learnCards(frame, words)

def outputLearn(name):
    for i in name/2:
        if(cardDis['text']==name[i]):
            cardDis['text']=name[i+1]
        else:
            cardDis['text']=name[i]