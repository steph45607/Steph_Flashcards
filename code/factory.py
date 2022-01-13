from tkinter import *

from methods import *
from frames import *
"""
Class to create object of deck card
"""
class Deck():
    # Initialization
    def __init__(self, frame, name, list):
        self.__name = name
        self.__list = list
        self.__frame = frame
    # Getters
    def getName(self):
        return self.__name
    
    def getList(self):
        return self.__list
    # Setters
    def setName(self, name):
        self.__name = name

    def setList(self, list):
        self.__list = list
    # To create button
    def buttonMake(self, frame, name, list):
        # Create button name without \n
        name = name.strip("\n")
        # Create button with button widget tkinter
        # Command to learnCards page when clicked
        btn = Button(frame, text = name, command=lambda:frames.learnCards(frame, list), height=2, width=10).pack(side=TOP, pady=5)
