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
            if total + 10 < 21:
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

player = Player(name = 'user')
player.addCard(decks.pop())
player.addCard(decks.pop())
# do player stuff


dealer = Dealer(name = 'dealer')
dealer.addCard(decks.pop())
dealer.addCard(decks.pop())


print ('cards remaining {}'.format(len(decks)))

if dealer.bust():
    print ("Dealer Busts, players wins")

if not dealer.stand():
    dealer.addCard(decks.pop())

print (dealer.score())
