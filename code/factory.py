from methods import *
from tkinter import *
from frames import *
class Deck():
    def __init__(self, frame, name, list):
        self.__name = name
        self.__list = list
        self.__frame = frame
    
    def getName(self):
        return self.__name
    
    def getList(self):
        return self.__list

    def setName(self, name):
        self.__name = name

    def setList(self, list):
        self.__list = list
    
    def buttonMake(self, frame, name, list):
        name = name.strip("\n")
        btn = Button(frame, text = name, command=lambda:frames.learnCards(frame, list), height=2, width=10).pack(side=TOP, pady=5)
