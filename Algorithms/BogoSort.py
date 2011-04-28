from SortAlgorithm import SortAlgorithm
import random

class BogoSort(SortAlgorithm):
    """
    Implements bogo sort.
    O(n!) expected running time. Doesn't terminate in worst case.
    https://secure.wikimedia.org/wikipedia/en/wiki/Bogosort
    """
    def sort(self):
        l = self.items
        bubbleMarker = self.markers.addMarker(True, 0, (0, 0, 255))
        yield
        while not all(self.cmp.lte(x, y) for x, y in zip(l.items, l.items[1:])):
            for i in xrange(len(l.items)-1, -1, -1):
                l.swap(i, random.randint(0, i))
                self.markers.moveMarker(bubbleMarker, i)
                yield
