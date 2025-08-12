from random import *
import time

seed()
colors = ["red","blue","green","yellow", "black"]
specialcards = ["+4","colorchoose","dark hole"]
nums = [1,2,3,4,5,6,7,8,9]

class card:
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            self.cardcolor = colors[randint(0,4)]
            if self.cardcolor == "black":
                self.cardnum = specialcards[randint(0,2)]
            else:
                self.cardnum = randint(1,9)
            if self.cardcolor not in colors or (self.cardnum not in specialcards and self.cardnum not in nums):
                print("this card should not exist") 
        if len(args) == 2:
            self.cardcolor = args[0]
            self.cardnum = args[1]
            if self.cardcolor not in colors or (self.cardnum not in specialcards and self.cardnum not in nums):
                print("this card should not exist")
        if len(args) == 3:
            self.cardcolor = args[0]
            self.cardnum = args[1]
            if self.cardcolor == "black" and self.cardnum not in specialcards:
                print("warning this card is not regular")
                    
    def __repr__(self):
        return f"{self.cardcolor}:{self.cardnum}"
    
    def __eq__(self, othercard) -> bool:
        return self.cardcolor == othercard.cardcolor or self.cardcolor == "black"

class table:
    tradehub = []

    def __init__(self):
        self.deck = self.initialize_deck()
    def initialize_deck(self):
        new_deck = []
        for _ in range(100):
            new_deck.append(card())
        return new_deck
    
    def laycard(self):
        self.topcard = self.deck[0]
        self.deck.pop(0)


class Player:
    def __init__(self,hand, playernumber: int) -> None:
        self.hand = hand
        self.playernumber = playernumber

    

Table1 = table()
Table1.initialize_deck()
Table1.laycard()

print(Table1.topcard)







