from math import floor
from SortAlgorithm import SortAlgorithm

class RunSort(SortAlgorithm):
    """
    Implements runsort, using the accumulator approach.
    A faster implementation would be to use a binary merge,
    similar to that of merge sort.
    https://www.scss.tcd.ie/publications/tech-reports/reports.05/TCD-CS-2005-34.pdf
    """

    def sort(self):
        yield
        for x in self.runsort(0, len(self.items.items) - 1):
            yield

    def runsort(self, p, r):
        if self.cmp.lt(p, r):
            if self.cmp.lte(self.items.items[p], self.items.items[p+1]):
                q = self.split_rising_run(p, self.items.items)
            elif self.cmp.gt(self.items.items[p], self.items.items[p+1]):
                q = self.split_falling_run(p, self.items.items)

            split = self.markers.addMarker(True, q+1, (255, 0, 0))

            for x in self.runsort(q+1, r):
                yield
            self.markers.removeMarker(split)
            for x in self.merge(p, q, r):
                yield

    def merge(self, p, q, r):
        (L, R) = (self.items.items[p:q+1], self.items.items[q+1:r+1])

        L[len(L):] = [float('infinity')]
        R[len(R):] = [float('infinity')]

        kMarker = self.markers.addMarker(True, p, (0, 0, 255))

        i = j = 0
        for k in range(p, r+1):
            self.markers.moveMarker(kMarker, k+1)
            if self.cmp.lte(L[i], R[j]):
                self.items.items[k] = L[i]
                i += 1
            else:
                self.items.items[k] = R[j]
                j += 1
            yield

        self.markers.removeMarker(kMarker)

    def split_falling_run(self, p, l):
        sublist = []
        sublist.append(l[p+1])
        sublist.append(l[p])

        t = p
        p += 1
        while p+1 < len(l) and self.cmp.gt(l[p], l[p+1]):
            p += 1
            sublist.insert(0, l[p])

        for i in sublist:
            self.items.items[t] = i
            t += 1

        return p

    def split_rising_run(self, p, l):
        self.items.items[p] = l[p]
        self.items.items[p+1] = l[p+1]

        p += 1
        while p+1 < len(l) and self.cmp.lte(l[p], l[p+1]):
            p += 1
            self.items.items[p] = l[p]

        return p
