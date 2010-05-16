from SortAlgorithm import SortAlgorithm

class BinaryInsertionSort(SortAlgorithm):
    """
    Implements binary insertion sort.
    O(n^2), non-stable, in-place
    http://www.brpreiss.com/books/opus5/html/page487.html
    """
    def sort(self):
        yield
        iMarker = self.markers.addMarker(True, 0, (255, 0, 0))
        for i in range(1, len(self.items.items)):
            self.markers.moveMarker(iMarker, i+1)
            yield

            # indices 0 .. i-1 are sorted
            # wish to find where i is to be placed
            left = 0
            right = i

            leftMarker  = self.markers.addMarker(True, left, (12, 35, 204))
            rightMarker = self.markers.addMarker(True, right+1, (12, 35, 204))
            yield
            midMarker = self.markers.addMarker(False, 0, (0, 186, 16))

            while self.cmp.lt(left, right):
                mid = (left + right) // 2
                if self.cmp.ltI(mid, i):
                    left = mid + 1
                else:
                    right = mid

                self.markers.moveMarker(midMarker, mid)
                self.markers.moveMarker(leftMarker, left)
                self.markers.moveMarker(rightMarker, right)
                yield

            self.markers.removeMarker(midMarker)
            self.markers.removeMarker(leftMarker)
            self.markers.removeMarker(rightMarker)

            pos = left
            # move the element at position i to position pos, then
            # shift the rest of the elements down
            posMarker = self.markers.addMarker(False, pos, (12, 35, 204))
            yield
            while pos < i:
                self.items.swap(pos, i)
                pos += 1
                self.markers.moveMarker(posMarker, pos)
                yield

            self.markers.removeMarker(posMarker)

        self.markers.removeMarker(iMarker)
