from SortAlgorithm import SortAlgorithm
import math

class IntroSort(SortAlgorithm):
    """
    Implements IntroSort.
    http://en.wikipedia.org/wiki/Introsort

    Implementation based off of the description of the one used in the
    GNU Standard C++ library: First QuickSort-like partitioning to a
    maximum depth of 2*log(n), where n is the number of elements,
    followed by an InsertionSort.
    """

    done = False

    def sort(self):
        yield
        maxdepth = math.floor(math.log(len(self.items.items))) * 2
        for x in self.introsort(0, len(self.items.items) - 1, maxdepth):
            yield

    def introsort(self, p, r, maxdepth):
        if not self.done:
            if maxdepth == 0:
                # InsertionSort
                for x in self.insertionsort():
                    yield
                self.done = True
            else:
                # Quicksort
                for x in self.partition(p, r):
                    q = x
                    yield
                for x in self.introsort(p, q-1, maxdepth - 1):
                    yield
                for x in self.introsort(q+1, r, maxdepth - 1):
                    yield

    def partition(self, p, r):
        i = p - 1
        iMarker = self.markers.addMarker(True, i+1, (128, 0, 128))
        jMarker = self.markers.addMarker(True, p, (0, 0, 255))
        pivotMarker = self.markers.addMarker(False, r, (219, 110, 255))
        for j in range(p, r):
            self.markers.moveMarker(jMarker, j)
            if self.cmp.lteI(j, r):
                i += 1
                self.items.swap(i, j)
                self.markers.moveMarker(iMarker, i+1)
            yield
        self.items.swap(i+1, r)
        self.markers.removeMarker(iMarker)
        self.markers.removeMarker(jMarker)
        self.markers.moveMarker(pivotMarker, i+1)
        yield i+1
        self.markers.removeMarker(pivotMarker)

    def insertionsort(self):
        yield
        iMarker = self.markers.addMarker(True, 0, (255, 0, 0))
        for i in range(1, len(self.items.items)):
            self.markers.moveMarker(iMarker, i+1)
            yield
            j = i - 1
            jMarker = self.markers.addMarker(False, j, (255, 159, 0))
            while self.cmp.gte(j, 0) and self.cmp.gtI(j, j+1):
                self.items.swap(j, j+1)
                yield
                j -= 1
                self.markers.moveMarker(jMarker, j)
            yield
            self.markers.removeMarker(jMarker)
        self.markers.removeMarker(iMarker)
