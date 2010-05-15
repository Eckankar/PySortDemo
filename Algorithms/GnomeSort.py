from SortAlgorithm import SortAlgorithm

class GnomeSort(SortAlgorithm):
    """
    Implements gnome sort.
    O(n^2), stable, in-place
    http://en.wikipedia.org/wiki/Gnome_sort
    """
    def sort(self):
        yield

        i = 0
        iMarker = self.markers.addMarker(False, 0, (255, 0, 0))
        newMarker = self.markers.addMarker(False, 1, (0, 128, 0))

        while i < len(self.items.items):
            self.markers.moveMarker(iMarker, i)

            if self.cmp.eq(i, 0) or self.cmp.lteI(i-1, i):
                i += 1
            else:
                self.items.swap(i-1, i)
                i -= 1

            self.markers.moveMarker(newMarker, i)
            yield
