from random import random

class Orderable:
    """
    Container for the items we wish to sort.
    Items are stored in the field 'items'.
    Mostly here to keep track of number of swaps (stored in 'swaps').
    """
    def __init__(self, n):
        self.items = [random() for i in range(n)]
        self.swaps = 0

    def swap(self, i, j):
        """ Swaps the items in spots i and j. """
        self.swaps += 1
        (self.items[i], self.items[j]) = (self.items[j], self.items[i])
