import random
from card import Card

class Deck:
    def __init__(self, jokers):
        self.__jokers = jokers
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        if self.__jokers:
            numOfCards = 54
        else:
            numOfCards = 52

        for i in range(numOfCards):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()
