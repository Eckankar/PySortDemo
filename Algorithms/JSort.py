from InsertionSort import InsertionSort
from HeapSort import HeapSort

class JSort(InsertionSort, HeapSort):
    """
    Implements JSort.
    O(n^2)?, non-stable, in-place
    http://home.westman.wave.ca/~rhenry/sort/src/JSortAlgorithm.java
    """

    def sort(self):
        yield
        for x in self.jsort(len(self.items.items) - 1):
            yield

    def jsort(self, length):
        for x in self.buildHeap(isDown=True, isMax=False):
            yield
        for x in self.buildHeap(isDown=False, isMax=True):
            yield
        for x in self.insertionSort():
            yield
