from typing import Literal
from ast import *
from factory import *

buttons = []
with open("test.txt") as lst, open("test2.txt") as strg:
        name = lst.readlines()
        words = strg.readlines()
        for i in range(len(name)):
            # words[i] = literal_eval(words[i])
            buttons.append(name[i])
            # print(words[i])
            cards = Deck(name[i], words[i])
            buttons.append(cards)