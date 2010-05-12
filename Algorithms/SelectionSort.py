from SortAlgorithm import SortAlgorithm

class SelectionSort(SortAlgorithm):
    def sort(self):
        yield
        for i in range(0, len(self.items.items)):
            min = i
            jMarker = self.markers.addMarker(True, i, (255, 0, 0))
            minMarker = self.markers.addMarker(False, i, (255, 159, 0))
            for j in range(i, len(self.items.items)):
                self.markers.moveMarker(jMarker, j+1)
                if self.cmp.gtI(min, j):
                    min = j
                    self.markers.moveMarker(minMarker, j)
                yield

            self.markers.removeMarker(jMarker)
            self.markers.removeMarker(minMarker)

            self.items.swap(i, min)
            self.markers.addMarker(False, i, (0, 255, 0))
            yield
