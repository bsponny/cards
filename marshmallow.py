from deck import Deck

def printHands(hand, flipped, you):
    if you:
        player = "Your Hand:\n"
    else:
        player = "Computer's Hand:\n"

    for i in range(len(hand)):
        if flipped[i]:
            player += str(hand[i])
        else:
            player += " *** "
    print(player)

def deal(deck):
    hand = []

    for i in range(10):
        hand.append(deck.draw())
    return hand

def setUp():
    flipped = []

    for i in range(10):
        flipped.append(False)
    return flipped

def turn(card, hand, flipped):
    cardValue = card.getCardValue()
    if cardValue > 10:
        return hand, flipped, card
    index = cardValue - 1

    while not flipped[index]:
        oldCard = hand[index]
        hand[index] = card
        flipped[index] = True
        card = oldCard
        cardValue = card.getCardValue()

        if cardValue > 10:
            return hand, flipped, card

        index = cardValue - 1
        print("The card from your hand is the " + str(card))

    return hand, flipped, card

def main():
    deck = Deck(False)
    deck.shuffle()

    playerFlipped = setUp()
    computerFlipped = setUp()

    playing = True
    while playing:
        if not False in playerFlipped:
            print("You win!!")
            print("Thanks for playing!")
            playing = False
            break

        elif not False in computerFlipped:
            print("Sorry. You lost.")
            print("Thanks for playing though.")
            playing = False
            break

        else:
            playerHand = deal(deck)
            computerHand = deal(deck)

            discard = deck.draw()

            printHands(playerHand, playerFlipped, True)
            printHands(computerHand, computerFlipped, False)

            drawQuestion = int(input("Do you want to (1) pick up the " + str(discard) + "or (2) draw a new card? "))

            if drawQuestion == 1:
                newCard = discard
                drew = "picked up"
            else:
                newCard = deck.draw()
                drew = "drew"

            print("You " + drew + " the " + str(newCard))

            playerHand, playerFlipped, discard = turn(newCard, playerHand, playerFlipped)

            printHands(playerHand, playerFlipped, True)
            printHands(computerHand, computerFlipped, False)

            print("\nNow it's the computer's turn!\n")

            cardValue = discard.getCardValue()
            index = cardValue - 1
            if cardValue < 11:
                if not computerFlipped[index]:
                    computerHand, computerFlipped, discard = turn(discard, computerHand, computerFlipped)


main()
