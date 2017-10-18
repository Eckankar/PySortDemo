from SortAlgorithm import SortAlgorithm


class CircleSort(SortAlgorithm): 
    """
    Implements circle sort.
    O(n lg n)
    http://www.geeksforgeeks.org/circle-sort/
    """

    swaps = 1

    def sort(self):
        while self.swaps:
            self.swaps = 0
            yield
            for x in self.CircleSort(0, len(self.items.items) - 1):
                yield
            self.markers.removeAllMarkers()

    def CircleSort(self, p, r):
        if self.cmp.eq(p, r):
            return
        pMarker = self.markers.addMarker(False, p, (0, 0, 255))
        rMarker = self.markers.addMarker(False, r, (0, 0, 255))
        yield
        high = r
        low = p
        mid = int((r-p)/2)
        while self.cmp.lt(p, r):
            if self.cmp.gtI(p, r):
                self.items.swap(p, r)
                self.swaps += 1
            p += 1
            r -= 1
            self.markers.moveMarker(pMarker, p)
            self.markers.moveMarker(rMarker, r)
            yield

        if self.cmp.eq(p, r):
            self.markers.moveMarker(rMarker, r+1)
            if self.cmp.gtI(p, r+1):
                self.items.swap(p, r+1)
                self.swaps +=1
            yield

        self.markers.removeMarker(pMarker)
        self.markers.removeMarker(rMarker)
        split = self.markers.addMarker(True, low+mid+1, (255, 0, 0))
        yield

        for x in self.CircleSort(low,low+mid):
            yield
        for x in self.CircleSort(low+mid+1,high):
            yield