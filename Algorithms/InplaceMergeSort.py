from math import floor
from SortAlgorithm import SortAlgorithm

class InplaceMergeSort(SortAlgorithm):
    """
    Implements in-place merge sort.
    O(n lg n), stable, in-place
    http://www.cs.ubc.ca/~harrison/Java/MergeSortAlgorithm.java.html
    """

    def sort(self):
        for x in self.inplacemergesort(0, len(self.items.items) - 1):
            yield

    def inplacemergesort(self, lo, hi):
        if self.cmp.lt(lo, hi):
            mid = int(floor((lo+hi)/2))
            split = self.markers.addMarker(True, mid+1, (0, 0, 255))
            yield
            for x in self.inplacemergesort(lo, mid):
                yield
            for x in self.inplacemergesort(mid+1, hi):
                yield
            self.markers.removeMarker(split)

            """ Merging the two sorted lists """

            end_lo = mid
            start_hi = mid+1
            loMarks = []
            loMarker = self.markers.addMarker(False, lo, (0, 255, 0))
            hiMarker = self.markers.addMarker(False, start_hi, (255, 0, 0))

            while (lo <= end_lo and start_hi <= hi):
                self.markers.moveMarker(loMarker, lo)
                self.markers.moveMarker(hiMarker, start_hi)
                yield

                if self.cmp.lteI(lo,start_hi):
                    loMarks.append( self.markers.addMarker(False, lo, (0, 200, 0)) )
                    lo += 1
                    yield
                else:
                    for k in range(start_hi-1,lo-1,-1):
                        self.items.swap(k, k+1)
                        self.markers.moveMarker(hiMarker, k)
                        yield
                    loMarks.append( self.markers.addMarker(False, lo, (0, 200, 0)) )
                    lo += 1
                    end_lo += 1
                    start_hi += 1
            for mark in loMarks:
                self.markers.removeMarker(mark)
            self.markers.removeMarker(loMarker)
            self.markers.removeMarker(hiMarker)
