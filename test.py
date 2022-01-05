from tkinter import filedialog
import os

def readFile():
    file = "sample/notes.txt"
    with open("storage/cardlist.txt", "a") as f:
        f.write(os.path.splitext(os.path.basename(file))[0]+"\n")

    with open(file, "r") as f:
        
        global words
        words = []
        for i in f:
            i = i.replace("\n","")
            words.append(i)
    
        for i in range(len(words)):
            words[i] = words[i].split("\\")

        

        # frames.learnCards(frame, words)
        print(words[0][0])
        print(len(words))

readFile()

global words
for i in range(len(words)):
    print(words[i][0])
    print(words[i][1])
    print("next")