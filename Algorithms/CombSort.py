from SortAlgorithm import SortAlgorithm

class CombSort(SortAlgorithm):
    """
    Implements comb sort.
    O(n^2)
    https://secure.wikimedia.org/wikipedia/en/wiki/Comb_sort
    """
    def sort(self):
        yield

        gap = len(self.items.items)
        swaps = False

        gapmarker = self.markers.addMarker(False, gap, (255, 0, 255))
        imarker = self.markers.addMarker(False, 0, (255, 0, 0))

        while gap != 1 or not swaps:
            gap = int(gap / 1.247330950103979)
            if gap < 1:
                gap = 1

            i = 0
            swaps = False


            while i+gap < len(self.items.items):
                self.markers.moveMarker(imarker, i)
                self.markers.moveMarker(gapmarker, gap+i)
                if self.cmp.gtI(i, i+gap):
                    self.items.swap(i, i+gap)
                    swaps = True
                    yield
                i += 1
