from math import floor

class MergeSort:
    def initialize(self, cmp, items):
        self.cmp = cmp
        self.items = items
        
    def sort(self): 
        yield
        for x in self.mergesort(0, len(self.items.items) - 1):
            yield
            
    def mergesort(self, p, r):
        if self.cmp.lt(p, r):
            q = int(floor((p+r)/2))
            for x in self.mergesort(p, q):
                yield
            for x in self.mergesort(q+1, r):
                yield
            for x in self.merge(p, q, r):
                yield
                
    def merge(self, p, q, r):
        (L, R) = (self.items.items[p:q+1], self.items.items[q+1:r+1])
        
        L[len(L):] = [float('infinity')]
        R[len(R):] = [float('infinity')]
        
        i = j = 0
        for k in range(p, r+1):
            if self.cmp.lte(L[i], R[j]):
                self.items.items[k] = L[i]
                i += 1
            else:
                self.items.items[k] = R[j]
                j += 1
            yield
