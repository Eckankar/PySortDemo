from math import floor
from SortAlgorithm import SortAlgorithm


class MergeSort(SortAlgorithm):
    """
    Implements merge sort.
    O(n lg n), stable, not in-place
    http://en.wikipedia.org/wiki/Merge_sort
    """
    def sort(self):
        yield
        for x in self.mergesort(0, len(self.items.items) - 1):
            yield

    def mergesort(self, p, r):
        if self.cmp.lt(p, r):
            q = int(floor((p+r)/2))
            split = self.markers.addMarker(True, q+1, (255, 0, 0))
            for x in self.mergesort(p, q):
                yield
            for x in self.mergesort(q+1, r):
                yield
            self.markers.removeMarker(split)
            for x in self.merge(p, q, r):
                yield

    def merge(self, p, q, r):
        (L, R) = (self.items.items[p:q+1], self.items.items[q+1:r+1])

        L[len(L):] = [float('infinity')]
        R[len(R):] = [float('infinity')]

        kMarker = self.markers.addMarker(True, p, (0, 0, 255))

        i = j = 0
        for k in range(p, r+1):
            self.markers.moveMarker(kMarker, k+1)
            if self.cmp.lte(L[i], R[j]):
                self.items.items[k] = L[i]
                i += 1
            else:
                self.items.items[k] = R[j]
                j += 1
            yield

        self.markers.removeMarker(kMarker)
