from typing import Deque
import random


SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
          "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]


class Card:

    # Card constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Returns the suit of the card.
    def suit(self):
        return self.suit

    # Returns the value of the card.
    def value(self):
        return self.value

    def __repr__(self):
        return f'Card(suit={self.suit}, value={self.value})'


class Deck(Card):

    cards = Deque()
    # Creates a sorted deck of playing cards. 13 values, 4 suits.

    def __init__(self):
        for i in range(0, len(SUITS)):
            for j in range(0, len(VALUES)):
                self.cards.append(Card(SUITS[i], VALUES[j]))

    # Returns the number of Cards in the Deck
    def allcards(self):
        return self.cards

    def num_cards(self):
        return len(self.cards)

    # Shuffles the deck of cards.
    def shuffle(self):
        random.shuffle(self.cards)

    # Returns the top Card in the deck, then puts it back.
    def peek(self):
        return self.cards[-1]

    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        return self.cards.pop()

    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if len(self.cards) > 52:
            raise Exception
        else:
            self.cards.append(card)

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        for i in range(0, len(self.cards)):
            print(self.cards[i])


deck = Deck()
print(deck.num_cards())
deck.shuffle()
draw = deck.draw()
print("draw = {}, it is in deck: {}".format(draw, (draw in deck.allcards())))
D6 = Card("DIAMONDS", "SIX")
deck.add_card(D6)
print(deck.peek())
deck.print_deck()
