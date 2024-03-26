import random
from card import Card

class Deck:
    def __init__(self, jokers):
        self.__jokers = jokers
        self.__deck = []
        if self.__jokers:
            numOfCards = 54
        else:
            numOfCards = 52

        for i in range(numOfCards):
            self.__deck.append(Card(i))

    def shuffle(self):
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()

    def printDeck(self):
        for i in range(len(self.__deck)):
            print(self.__deck[i])
