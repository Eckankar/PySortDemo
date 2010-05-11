from SortAlgorithm import SortAlgorithm

class SelectionSort(SortAlgorithm):
    def sort(self): 
        yield
        for i in range(0, len(self.items.items)):
            min = i
            for j in range(i, len(self.items.items)):
                if self.cmp.gtI(min, j):
                    min = j
            self.items.swap(i, min)
            yield
