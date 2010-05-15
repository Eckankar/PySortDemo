from math import floor
from SortAlgorithm import SortAlgorithm

class InsertionMergeSort(SortAlgorithm):
    """
    Implements a merge sort/insertion sort hybrid.
    O(?), ?-stable, not in-place

    Merge sort is used for the sorting, until the size of what needs to be
    sorted falls below a certain threshold, after which insertion sort is used.
    """

    THRESHOLD = 10

    def sort(self):
        yield
        for x in self.sortInterval(0, len(self.items.items) - 1):
            yield

    def sortInterval(self, p, r):
        """
        Sorts the interval using mergesort if the length > THRESHOLD, 
        else using insertion sort.
        """
        if self.cmp.lt(r-p, self.THRESHOLD):
            for x in self.insertionSort(p, r):
                yield
        else:
            for x in self.mergeSort(p, r):
                yield

    def insertionSort(self, p, r):
        """ Insertion sorts the interval with indices [p, ..., r] """
        iMarker = self.markers.addMarker(True, 0, (0, 0, 255))
        for i in range(p, r+1):
            self.markers.moveMarker(iMarker, i+1)
            yield
            j = i - 1
            jMarker = self.markers.addMarker(False, j, (255, 159, 0))
            while self.cmp.gte(j, p) and self.cmp.gtI(j, j+1):
                self.items.swap(j, j+1)
                yield
                j -= 1
                self.markers.moveMarker(jMarker, j)
            yield
            self.markers.removeMarker(jMarker)
        self.markers.removeMarker(iMarker)

    def mergeSort(self, p, r):
        """ Merge sorts the interval with indices [p, ..., r] """
        if self.cmp.lt(p, r):
            q = int(floor((p+r)/2))
            split = self.markers.addMarker(True, q+1, (255, 0, 0))
            for x in self.sortInterval(p, q):
                yield
            for x in self.sortInterval(q+1, r):
                yield
            self.markers.removeMarker(split)
            for x in self.merge(p, q, r):
                yield

    def merge(self, p, q, r):
        """
        Performs a merge on the two intervals with indices
        [p, ..., q] and [q+1, ..., r]. (Not in-place.)
        """

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

