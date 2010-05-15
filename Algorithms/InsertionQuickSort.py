from SortAlgorithm import SortAlgorithm

class InsertionQuickSort(SortAlgorithm):
    """
    Implements a quicksort/insertion sort hybrid.
    O(?), ?-stable, in-place

    Quicksort is used for the sorting, until the size of what needs to be
    sorted falls below a certain threshold, after which insertion sort is used.
    """

    THRESHOLD = 10

    def sort(self):
        yield
        for x in self.sortInterval(0, len(self.items.items) - 1):
            yield

    def sortInterval(self, p, r):
        """
        Sorts the interval using quicksort if the length > THRESHOLD, 
        else using insertion sort.
        """
        if self.cmp.lt(r-p, self.THRESHOLD):
            for x in self.insertionSort(p, r):
                yield
        else:
            for x in self.quickSort(p, r):
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


    def quickSort(self, p, r):
        """ Quicksorts the interval with indices [p, ..., r] """
        topMarker = self.markers.addMarker(True, p, (255, 0, 0))
        bottomMarker = self.markers.addMarker(True, r+1, (255, 0, 0))
        if self.cmp.lt(p, r):
            for x in self.partition(p, r):
                q = x
                yield
            for x in self.sortInterval(p, q-1):
                yield
            for x in self.sortInterval(q+1, r):
                yield
        self.markers.removeMarker(topMarker)
        self.markers.removeMarker(bottomMarker)

    def partition(self, p, r):
        """ Partitions the interval with indices [p, ..., r] for quicksort """
        i = p - 1
        iMarker = self.markers.addMarker(True, i+1, (128, 0, 128))
        jMarker = self.markers.addMarker(True, p, (0, 0, 255))
        pivotMarker = self.markers.addMarker(False, r, (0, 255, 0))
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
