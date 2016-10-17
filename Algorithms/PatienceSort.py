from math import floor
from SortAlgorithm import SortAlgorithm


class PatienceSort(SortAlgorithm):
    """
    Implements patience sorting.
    http://en.wikipedia.org/wiki/Patience_sorting
    """

    piles = []
    pileMarkers = []

    def sort(self):
        yield
        pileMarker = self.markers.addMarker(True, 0, (255,0,0))
        self.pileMarkers.append(pileMarker)
        self.piles.append(0)
        yield
        for x in self.patiencesort(self.items.items):
            yield

    def patiencesort(self, a):
        itemMarker = self.markers.addMarker(False, 0, (0,255,0))

        for p in range(1 ,len(a)):
            self.markers.moveMarker(itemMarker, p)
            yield
            foundPile = False
            for key,pile in enumerate(self.piles):
                if self.cmp.lteI(p, pile):
                    for i in range(pile, p):
                        self.items.swap(p, p-1)
                        p = p-1
                        self.markers.moveMarker(itemMarker, p)

                    # Move all piles in front of the pile in question
                    for j in range(key+1, len(self.piles)):
                        #print("Moving pile j=%d to j+1=%d" % (j, j+1))
                        self.piles[j] = self.piles[j] + 1
                        self.markers.moveMarker(self.pileMarkers[j], self.piles[j])
                    yield

                    foundPile = True
                    break

            if not foundPile:
                #print("Created new pile with p=%d" % p)
                self.piles.append(p)
                pileMarker = self.markers.addMarker(True, p, (255, 0, 0))
                self.pileMarkers.append(pileMarker)
                yield

            self.markers.moveMarker(itemMarker, p+1)

        self.markers.removeMarker(itemMarker)


        for x in self.merge(0, len(self.items.items)):
            yield
        

    def merge(self, p, q):
        if self.cmp.lt(p, q):
            smallest = self.piles[0]
            smallestKey = 0
            smallestIndex = 0
            for pile in self.piles:
                # Choose smallest
                if self.cmp.lteI(pile, smallest):
                    smallest = pile
                    smallestKey = smallestIndex
                smallestIndex += 1

            # Advance piles
            for k in range(smallestKey, -1, -1):
                if (self.cmp.lt(k, len(self.piles)-1) and 
                self.cmp.lt(self.piles[k]+1, self.piles[k+1]) or
                self.cmp.lt(self.piles[k], len(self.items.items)-1)):
                    #print("Advance pile at key: %d" % (k))
                    self.piles[k] += 1
                    self.markers.moveMarker(self.pileMarkers[k], self.piles[k])
                else:
                    #print("Pile with key %d empty, deleting" % (k))
                    del self.piles[k]
                    self.markers.removeMarker(self.pileMarkers[k])
                    del self.pileMarkers[k]

            # Swap
            for s in range(p, smallest):
                self.items.swap(smallest, smallest-1)
                smallest = smallest - 1

            yield

            for x in self.merge(p+1, len(self.items.items)):
                yield
