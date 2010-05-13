from SortAlgorithm import SortAlgorithm

class BidirectionalBubbleSort(SortAlgorithm):
    """
    Implements cocktail sort.
    O(n^2), stable, in-place
    http://en.wikipedia.org/wiki/Cocktail_sort

    Basically a bubblesort that alternates between bubbling up and down.
    """
    def sort(self):
        yield
        goingDown = True
        changed = True
        p = 0
        r = len(self.items.items)-1
        while p != r and changed:
            changed = False
            if goingDown:
                bubbleMarker = self.markers.addMarker(False, p, (255, 0, 0))
                for i in range(p, r):
                    if self.cmp.gtI(i, i+1):
                        self.items.swap(i, i+1)
                        changed = True
                    self.markers.moveMarker(bubbleMarker, i+1)
                    yield
                self.markers.addMarker(False, r, (0, 255, 0))
                r -= 1
            else:
                bubbleMarker = self.markers.addMarker(False, r, (255, 0, 0))
                for i in range(r, p, -1):
                    if self.cmp.gtI(i-1, i):
                        self.items.swap(i-1, i)
                        changed = True
                    self.markers.moveMarker(bubbleMarker, i-1)
                    yield
                self.markers.addMarker(False, p, (0, 255, 0))
                p += 1

            self.markers.removeMarker(bubbleMarker)
            goingDown = not goingDown
            yield

