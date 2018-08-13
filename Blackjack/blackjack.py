#!/usr/bin/python3

import random


class Deck(object):
    def __init__(self, qty = 1):
        self.cards = ['2','3','4','5','6','7','8','9','10',
                      'J','Q','K','A']
        self.deck = self.cards * 4 * qty
        self.deck = random.sample(self.deck, k = len(self.deck))

    def getDecks(self):
        return self.deck


class Player(object):
    def __init__(self, hand= [], name =  ""):
        self.hand = hand
        self.name = name


    def score(self):
        '''Get the score of the hand'''

        cards = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 1
        }

        total = 0
        for card in self.hand:
            total += cards[card]

        if 'A' in self.hand:
            if total + 10 < 22:
                return total + 10
        else:
            return total

    def addCard(self,card):
        self.hand.append(card)

class Dealer(Player):
    def __init__ (self, hand = [], name = ""):
        Player.__init__(self,hand, name)

    def bust(self):
        if self.score() > 21:
            return True
        return False

    def stand(self):
        if self.score() > 16:
            return True
        return False

# 6 deck game is most popular
decks = Deck(6).getDecks()
draws = 0
playerWins = 0
dealerWins = 0
for i in range (0,200):

    # set up the player cards
    player = Player(name = 'user', hand = [])
    player.addCard(decks.pop())
    player.addCard(decks.pop())
    # do player stuff

    # set up the dealer cards

    dealer = Dealer(name = 'dealer', hand = [])
    dealer.addCard(decks.pop())
    dealer.addCard(decks.pop())

    print (player.hand)
    # lets test auto with a player score of under 12 hitt
    while player.score() < 13:

        player.addCard(decks.pop())


    print ('cards remaining {}'.format(len(decks)))

    dPlaying = "playing"
    # have the dealer play
    while dPlaying == "playing":

    #    print  ("\nThe dealers hand is {}".format(" ".join(str(e) for e in dealer.hand)))
    #    print ("Current dealers score is {}".format(dealer.score()))
        if dealer.bust():
    #        print ("Dealer Busts, players wins")
            winner = "Player"
            dPlaying = False
            continue
        if dealer.stand():
            dPlaying = False
            continue
        dealer.addCard(decks.pop())
    #    print ("*" * 30)

    print ("#" * 45)
    print ("#" * 45)
    print ("\n")
    print ("Players hand {} with a total of {}".format(" ".join(str(e) for e in player.hand), player.score()))

    print ("Dealers hand {} with a total of {}".format(" ".join(str(e) for e in dealer.hand), dealer.score()))
    print ("\n")
    print ("#" * 45)
    print ("#" * 45)



    if not dealer.bust():
        if dealer.score() > player.score():
            winner = "dealer"
            dealerWins += 1
        elif dealer.score() == player.score():
            winner = "draw"
            draws += 1
        else:
            winner = "player"
            playerWins += 1

    #if winner == "draw":
    #    print ("There was a draw")
    #else:
    #    print ("The winner is {}".format(winner))
    if len(decks) < 200:

        decks = Deck(6).getDecks()
