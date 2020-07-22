# Deck Class
#   * Instantite a new deck
#       * Create all 52 card objects
#       * Hold as a list of card objects
#   * Shuffle a deck through a method call
#       * Random library shuffle() function
#   * Deal cards from the Deck object
#       * Pop method from cards list
import random
from card import Card
from card import suits
from card import ranks
from card import values


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_str = ""

        for card in self.all_cards:
            deck_str += str(card) + "\n"

        return deck_str
