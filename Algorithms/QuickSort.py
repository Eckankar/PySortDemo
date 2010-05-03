class QuickSort:
    def initialize(self, cmp, items):
        self.cmp = cmp
        self.items = items
        
    def sort(self): 
        yield
        for x in self.quicksort(0, len(self.items.items) - 1):
            yield
           
    def quicksort(self, p, r):
        if self.cmp.lt(p, r):
            for x in self.partition(p, r):
                q = x
                yield
            for x in self.quicksort(p, q-1):
                yield
            for x in self.quicksort(q+1, r):
                yield
    
    def partition(self, p, r):
        i = p - 1
        for j in range(p, r):
            if self.cmp.lteI(j, r):
                i += 1
                self.items.swap(i, j)
            yield
        self.items.swap(i+1, r)
        yield i+1