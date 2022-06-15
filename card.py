class Card:
    def __init__(self, value):
        self.__value = value
        self.__suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.__faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def getSuit(self):
        if self.__value != 52 and self.__value != 53:
            return self.__suits[self.__value // 13]
        else:
            return "Joker"

    def getFace(self):
        if self.__value != 52 and self.__value != 53:
            return self.__faces[self.__value % 13]
        else:
            return "Joker"

    def getCardValue(self):
        if self.__value != 52 and self.__value != 53:
            return self.__value % 13 + 1
        else:
            return 14

    def getDeckValue(self):
        return self.__value

    def __str__(self):
        if self.__value != 52 and self.__value != 53:
            return self.getFace() + " of " + self.getSuit() + "  "
        else:
            return "Joker"

