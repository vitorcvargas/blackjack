import random

class Card:

    suits = ['heart', 'diamonds', 'spades', 'clubs']
    ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']    

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
    
    def shuffle(self):
        random.shuffle(self.cards)


class Deck(Card):

    def __init__(self):
        self.cards = []

        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append(Card(rank,suit))


    def hit(self):
        card = self.cards.pop(0)    
        return card


class Chip:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def make_bet(self, value):
        enough_chips = True
        if value <= self.total:
            self.bet = value
        else:
            enough_chips = False
        return enough_chips

    def result(self, result):

        if result == True:
            self.total += self.bet
        else:
            self.total -= self.bet



def get_card_value(total, card):
    value = 0
    if card in [2,3,4,5,6,7,8,9,10]:
        value = card
    elif card in ['jack', 'queen', 'king']:
        value = 10
    else:
        if total <= 10:
            value = 11
        else:
            value = 1
    return value


def win(player_total, dealer_total):
    win = True
    if player_total > dealer_total:
        win = True
    elif player_total < dealer_total and dealer_total < 22:
        win = False
    return win
    

def bust(total):
    bust = False
    if total > 21:
        bust = True
    return bust







