"""
example usage:
>>> a_deck = FrenchDeck()
>>> len(a_deck)
52
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ['♣', '♠', '♥', '♦']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def random_choice(self):
        from random import choice

        return choice(self._cards)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
