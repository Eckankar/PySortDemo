from SortAlgorithm import SortAlgorithm

class InsertionSort(SortAlgorithm):
    """
    Implements insertion sort.
    O(n^2), stable, in-place
    http://en.wikipedia.org/wiki/Insertionsort
    """
    def sort(self):
        for x in self.insertionSort():
            yield

    def insertionSort(self):
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
