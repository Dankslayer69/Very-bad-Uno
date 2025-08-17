from random import *
import time

seed()
colors = ["red", "blue", "green", "yellow", "black"]
specialcards = ["+4", "colorchoose", "dark hole"]
nums = [1,2,3,4,5,6,7,8,9]

class card:
    # cardnum also represents black card properties not just numbers
    def __init__(self, *args, **kwargs):
        if len(args) == 0:  # random card
            self.cardcolor = colors[randint(0,4)]
            if self.cardcolor == "black":
                self.cardnum = specialcards[randint(0,2)]
            else:
                self.cardnum = randint(1,9)

        elif len(args) == 2:  # user-defined card
            self.cardcolor = args[0]
            self.cardnum = args[1]

        valid_card = True
        if self.cardcolor not in colors:
            valid_card = False
        if self.cardcolor == "black" and self.cardnum not in specialcards:
            valid_card = False
        if self.cardcolor != "black" and self.cardnum not in nums:
            valid_card = False

        if not valid_card:
            print(f"warning this {self.cardcolor}: {self.cardnum} should not exist")
                    
    def __repr__(self):
        return f"{self.cardcolor} : {self.cardnum}"
    
    def __eq__(self, othercard) -> bool:
        return (
            self.cardcolor == othercard.cardcolor
            or self.cardcolor == "black"
            or othercard.cardcolor == "black"
            or self.cardnum == othercard.cardnum
        )

class table:
    tradehub = []

    def __init__(self):
        self.deck = self.initialize_deck()
        self.topcard = None

    def initialize_deck(self):
        new_deck = []
        for _ in range(100):
            new_deck.append(card())
        return new_deck
    
    def laycard(self, playedcard):
        """Place a card on the table"""
        self.topcard = playedcard
        print(f"Table top card is now {self.topcard}")

class Player:
    def __init__(self, playernumber: int):
        self.hand = self.initialize_hand()
        self.playernumber = playernumber

    def initialize_hand(self):
        new_hand = []
        for i in range(9):
            new_hand.append(card())
        return new_hand

    def playcard(self, userindexinput: int):
        if 0 <= userindexinput < len(self.hand):
            return self.hand.pop(userindexinput)
        else:
            print("Invalid card index.")
            return None



if __name__ == "__main__":
    t = table()
    p1 = Player(1)

    print("Player 1 hand:", p1.hand)

    # Player plays first card
    played = p1.playcard(0)
    if played:
        t.laycard(played)

    print("Player 1 hand after playing:", p1.hand)
