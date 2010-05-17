from SortAlgorithm import SortAlgorithm
from time import sleep

class SillySort(SortAlgorithm):
    """
    Implements silly sort.
    O(n^(a lg n)), ?-stable, in-place
    http://home.tiac.net/~cri_d/cri/2001/badsort.html
    """
    def sort(self):
        yield
        for x in self.sillySort(0, len(self.items.items) - 1):
            yield

    def sillySort(self, p, r):
        for j in range(r, p, -1):
            m = p + (j - p) // 2
            for x in self.sillySort(p, m):
                yield
            for x in self.sillySort(m+1, j):
                yield
            if self.cmp.gtI(m, j):
                self.items.swap(m, j)
            yield
