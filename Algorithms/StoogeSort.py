from SortAlgorithm import SortAlgorithm

class StoogeSort(SortAlgorithm):
    """
    Implements Stooge sort
    O(n^(lg 3 / lg 1.5)), ?-stable, in-place
    http://en.wikipedia.org/wiki/Stooge_sort
    """
    def sort(self):
        for x in self.stoogeSort(0, len(self.items.items) - 1):
            yield

    def stoogeSort(self, left, right):
        leftMarker  = self.markers.addMarker(True, left, (0, 0, 255))
        rightMarker = self.markers.addMarker(True, right+1, (0, 0, 255))

        yield

        if self.cmp.gtI(left, right):
            self.items.swap(left, right)

        yield

        if self.cmp.gt(right - left, 1):
            third = (right - left + 1) // 3
            for x in self.stoogeSort(left, right - third):
                yield
            for x in self.stoogeSort(left + third, right):
                yield
            for x in self.stoogeSort(left, right - third):
                yield

        self.markers.removeMarker(leftMarker)
        self.markers.removeMarker(rightMarker)
