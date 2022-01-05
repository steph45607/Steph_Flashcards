from methods import *

class Deck():
    def __init__(self, name, list):
        self.__name = name
        self.__list = list
    
    def getName(self):
        print(self.name)
    
    def getList(self):
        print(self.list)

    def setName(self, name):
        self.__name = name

    def setList(self, list):
        self.__list = list

        

