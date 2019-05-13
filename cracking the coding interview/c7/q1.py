from random import shuffle

class Card:
    def __init__(self, suit, val):
        self.suit, self.val = suit, val

    def show(self):
        print(self.val, 'of ' + self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.cards.pop())

    def show_hand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()

player = Player('Shiny')
player.draw(deck)
player.show_hand()