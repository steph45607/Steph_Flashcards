from methods import *

class Deck():
    def __init__(self, name, list):
        self.__name = name
        self.__list = list
    
    def getName(self):
        return self.__name
    
    def getList(self):
        return self.__list

    def setName(self, name):
        self.__name = name

    def setList(self, list):
        self.__list = list
