from SortAlgorithm import SortAlgorithm


class BidirectionalSelectionSort(SortAlgorithm):
    """
    Implements bidirectional selection sort.
    O(n^2), stable, in-place
    http://en.wikipedia.org/wiki/Selection_sort#Variants
    """
    def sort(self):
        yield
        left = 0
        right = len(self.items.items)-1
        while left < right:
            min = left
            max = right

            minMarker = self.markers.addMarker(False, min, (202, 69, 255))
            maxMarker = self.markers.addMarker(False, max, (65, 114, 250))
            iMarker = self.markers.addMarker(True, left, (255, 0, 0))

            for i in range(left, right+1):
                self.markers.moveMarker(iMarker, i+1)
                if self.cmp.ltI(i, min):
                    min = i
                    self.markers.moveMarker(minMarker, i)
                if self.cmp.gteI(i, max):
                    max = i
                    self.markers.moveMarker(maxMarker, i)
                yield

            self.markers.removeMarker(iMarker)
            self.markers.removeMarker(minMarker)
            self.markers.removeMarker(maxMarker)

            self.items.swap(max, right)
            if self.cmp.eq(min, right):
                # we might've moved the minimum element in our first swap
                self.items.swap(max, left)
            else:
                self.items.swap(min, left)

            self.markers.addMarker(False, left, (0, 255, 0))
            self.markers.addMarker(False, right, (0, 255, 0))
            left += 1
            right -= 1
            yield
