from deck import Deck

def printHands(playerHands, cardsFlipped):
    for i in range(len(playerHands)):
        hand = "Player " + str(i + 1) + ": "
        for j in range(len(playerHands[i])):
            if cardsFlipped[i][j]:
                hand += str(playerHands[i][j])
            else:
                hand += " *** "
        print(hand)

def main():
    deck = Deck(True)
    validPlayers = False

    while not validPlayers:
        players = int(input("How many players? "))
        if players > 1 and players < 5:
            validPlayers = True
        else:
            print("Sorry. I need 2 - 4 players")
            validPlayers = False

    playerHands = []
    cardsFlipped = []
    playerLevels = []

    for i in range(players):
        playerHands.append([])
        cardsFlipped.append([])
        playerLevels.append(10)

    playing = True
    while playing:
        if (0 in playerLevels):
            playing = False
            print("Player " + str(playerLevels.index(0) + 1) + " wins!")
            print("Thanks for playing!")
            break

        discard = deck.draw()

        for player in range(players):
            for level in range(playerLevels[player]):
                playerHands[player].append(deck.draw())
                cardsFlipped[player].append(False)

        printHands(playerHands, cardsFlipped)

        playRound = True
        while playRound:
            for player in range(players):
                validAnswer = False
                while not validAnswer:
                    answer = int(input("Do you want to (1)Draw or (2) pick up the " + str(discard) + "? "))
                    if answer == 1:
                        newCard = deck.draw()
                        validAnswer = True
                    elif answer == 2:
                        newCard = discard
                        validAnswer = True
                    else:
                        print("Wrong answer. Try again")
                        validAnswer = False

                print("Drawn Card: " + str(newCard))

                while not (newCard.getCardValue() > 11 and newCard.getCardValue() < 14):
                    cardValue = newCard.getCardValue() - 1
                    tempCard = playersHand[player][cardValue]

                    if not cardsFlipped[player][cardValue]:
                        playersHand[player][cardValue] = newCard
                        newCard = tempCard

                        cardsFlipped[player][cardValue] = True
                        printHands(playerHands, cardsFlipped)
                    else:
                        if tempCard.getCardValue() == 11 or tempCard.getCardValue == 14:
                            playersHand[player][cardValue] = newCard
                            newCard = tempCard

                            cardsFlipped[player][cardValue] = True
                            printHands(playerHands, cardsFlipped)

                discard = newCard

                if player != players - 1:
                    print("Next Player!")

        playing = False

main()

