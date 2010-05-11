from SortAlgorithm import SortAlgorithm

class HeapSort(SortAlgorithm):
    def sort(self):
        yield
        for x in self.buildMaxHeap():
            yield
        for i in range(len(self.items.items) - 1, 0, -1):
            self.items.swap(0, i)
            yield
            for x in self.maxHeapify(0, i):
                yield

    def maxHeapify(self, i, heapSize):
        def left(i): return 2*i+1
        def right(i): return 2*(i+1)
        (l, r, largest) = (left(i), right(i), i)

        if self.cmp.lt(l, heapSize) and self.cmp.gtI(l, largest):
            largest = l

        if self.cmp.lt(r, heapSize) and self.cmp.gtI(r, largest):
            largest = r

        if largest != i:
            self.items.swap(i, largest)
            yield
            for x in self.maxHeapify(largest, heapSize):
                yield

    def buildMaxHeap(self):
        heapSize = len(self.items.items)
        for i in range(heapSize // 2 - 1, -1, -1):
            for x in self.maxHeapify(i, heapSize):
                yield
