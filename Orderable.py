from random import random

class Orderable:
    def __init__(self, n):
        self.items = [random() for i in range(n)]
        self.swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        (self.items[i], self.items[j]) = (self.items[j], self.items[i])
