from SortAlgorithm import SortAlgorithm

class ShellSort(SortAlgorithm):
    """
    Implements shell sort.
    O(n lg^2 n)*, non-stable, in-place
    http://en.wikipedia.org/wiki/Shell_sort

    * Given the right gap sizes.
    """
    def sort(self):
        yield
        hs = [1]
        h = 1
        while h*3 + 1 < len(self.items.items):
            h = h*3 + 1
            hs.append(h)
        hs.reverse()

        for step in hs:
            for start in range(0, step):
                    # Mark what we're sorting first
                    markers = []
                    for i in range(start, len(self.items.items), step):
                        markers.append(self.markers.addMarker(False, i, (255, 0, 0)))

                    positionMarker = self.markers.addMarker(True, 0, (0, 0, 255))

                    for i in range(start, len(self.items.items), step):
                        self.markers.moveMarker(positionMarker, i+1)
                        j = i - step
                        while self.cmp.gtI(j, j + step) and self.cmp.gte(j, start):
                            self.items.swap(j, j + step)
                            j -= step
                            yield
                        yield

                    # Clear the markers again
                    for marker in markers:
                        self.markers.removeMarker(marker)
                    self.markers.removeMarker(positionMarker)
