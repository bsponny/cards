# Cards

## Overview
This project is a deck of playing cards (in `deck.py` and `card.py`) and can be used by other files to program card games.

Creating a deck of cards in a game is done by importing the `Deck` class from `deck.py` and when creating the deck object, you pass in a boolean value of whether or not to have Jokers in the deck.
```
deck = Deck(True) # Creates a deck with Jokers

deck = Deck(False) # Creates a deck without Jokers
```
