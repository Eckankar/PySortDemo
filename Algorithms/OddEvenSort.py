from SortAlgorithm import SortAlgorithm

class OddEvenSort(SortAlgorithm):
    """
    Implements odd-even sort.
    O(n^2), ?-stable, in-place
    http://en.wikipedia.org/wiki/Odd-even_sort
    """
    def sort(self):
        yield
        changed = True

        itemCount = len(self.items.items)

        oddMarker = self.markers.addMarker(False, 1, (255, 0, 0))
        evenMarker = self.markers.addMarker(False, 2, (255, 0, 0))

        while changed:
            changed = False

            # odd-even pass
            for i in range(1, itemCount-1, 2):
                self.markers.moveMarker(oddMarker, i)
                self.markers.moveMarker(evenMarker, i+1)
                if self.cmp.gtI(i, i+1):
                    self.items.swap(i, i+1)
                    changed = True
                yield

            # even-odd pass
            for i in range(0, itemCount-1, 2):
                self.markers.moveMarker(evenMarker, i)
                self.markers.moveMarker(oddMarker, i+1)
                if self.cmp.gtI(i, i+1):
                    self.items.swap(i, i+1)
                    changed = True
                yield

        self.markers.removeMarker(oddMarker)
        self.markers.removeMarker(evenMarker)


