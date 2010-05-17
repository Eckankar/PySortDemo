from SortAlgorithm import SortAlgorithm

class QuickSort(SortAlgorithm):
    """
    Implements quicksort.
    O(n lg n), non-stable, in-place
    http://en.wikipedia.org/wiki/Quicksort

    Implementation based off of the one described in
    "Introduction to Algorithms" by Cormen et al.
    """
    def sort(self):
        yield
        for x in self.quicksort(0, len(self.items.items) - 1):
            yield

    def quicksort(self, p, r):
        topMarker = self.markers.addMarker(True, p, (255, 0, 0))
        bottomMarker = self.markers.addMarker(True, r+1, (255, 0, 0))
        if self.cmp.lt(p, r):
            for x in self.partition(p, r):
                q = x
                yield
            self.markers.addMarker(False, q, (0, 255, 0))
            for x in self.quicksort(p, q-1):
                yield
            for x in self.quicksort(q+1, r):
                yield
        else:
            self.markers.addMarker(False, p, (0, 255, 0))
        self.markers.removeMarker(topMarker)
        self.markers.removeMarker(bottomMarker)

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
