from ast import *
class Deck():
    def __init__(self, name, list):
        self.__name = name
        self.__list = list
    
    def getName(self):
        print(self.__name)
    
    def getList(self):
        self.__list = literal_eval(self.__list)
        print(self.__list)

    def setName(self, name):
        self.__name = name

    def setList(self, list):
        self.__list = list
