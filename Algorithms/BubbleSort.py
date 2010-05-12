from SortAlgorithm import SortAlgorithm

class BubbleSort(SortAlgorithm):
    def sort(self):
        yield
        changed = True
        i = len(self.items.items)
        while changed:
            changed = False
            bubbleMarker = self.markers.addMarker(False, 0, (255, 0, 0))
            for j in range(1, i):
                if self.cmp.gtI(j-1, j):
                    self.items.swap(j-1, j)
                    maxChanged = j
                    changed = True
                self.markers.moveMarker(bubbleMarker, j)
                yield
            self.markers.removeMarker(bubbleMarker)
            if changed:
                for x in range(maxChanged, i):
                    self.markers.addMarker(False, x, (0, 255, 0))
                i = maxChanged
