from SortAlgorithm import SortAlgorithm

class HeapSort(SortAlgorithm):
    """
    Implements heapsort.
    O(n lg n), non-stable, in-place
    http://en.wikipedia.org/wiki/Heapsort

    Implementation based off of the one described in
    "Introduction to Algorithms" by Cormen et al.
    """
    def sort(self):
        yield
        for x in self.buildHeap(isDown=True, isMax=True):
            yield
        for i in range(len(self.items.items) - 1, 0, -1):
            self.items.swap(0, i)
            self.markers.addMarker(False, i, (0, 255, 0))
            yield
            for x in self.heapify(0, i, isDown=True, isMax=True):
                yield

    def heapify(self, i, heapSize, isDown=True, isMax=True):
        def left(i): return 2*i+1
        def right(i): return 2*(i+1)

        (l, r, best) = (left(i), right(i), i)
        if not isDown:
            l = heapSize-l
            r = heapSize-r

        def inBounds(i): return self.cmp.lt(i, heapSize) if isDown else self.cmp.gte(i, 0)
        def isBetter(i): return self.cmp.gtI(i, best) if isMax else self.cmp.ltI(i, best)

        if inBounds(l) and isBetter(l): best = l
        if inBounds(r) and isBetter(r): best = r

        if best != i:
            self.items.swap(i, best)
            yield
            for x in self.heapify(best, heapSize, isDown, isMax):
                yield

    def buildHeap(self, isDown=True, isMax=True):
        heapSize = len(self.items.items)
        for i in range(heapSize // 2 - 1, -1, -1):
            for x in self.heapify(i if isDown else heapSize-i, heapSize, isDown, isMax):
                yield
