from math import floor
from SortAlgorithm import SortAlgorithm

class InplaceMergeSort(SortAlgorithm):
    """
    Implements in-place merge sort.
    O(n lg n), stable, in-place
    http://www.cs.ubc.ca/~harrison/Java/MergeSortAlgorithm.java.html    """

    def sort(self):
        yield
        for x in self.inplacemergesort(0, len(self.items.items) - 1):
            yield

    def inplacemergesort(self, lo, hi):
        if self.cmp.lt(lo, hi):
            mid = int(floor((lo+hi)/2))
            split = self.markers.addMarker(True, mid+1, (255, 0, 0))
            for x in self.inplacemergesort(lo, mid):
                yield
            for x in self.inplacemergesort(mid+1, hi):
                yield
            self.markers.removeMarker(split)

            """ Merging the two sorted lists """

            end_lo = mid
            start_hi = mid+1
            loMarker = self.markers.addMarker(True, lo, (0, 0, 255))
            while (lo <= end_lo and start_hi <= hi):
                self.markers.moveMarker(loMarker, lo)
                yield
                if self.cmp.lte(self.items.items[lo],self.items.items[start_hi]):
                    lo += 1
                    yield
                else:
                    temp = self.items.items[start_hi]
                    for k in range(start_hi-1,lo-1,-1):
                        self.items.items[k+1] = self.items.items[k]
                    self.items.items[lo] = temp
                    yield
                    lo += 1
                    end_lo += 1
                    start_hi += 1
            self.markers.removeMarker(loMarker)