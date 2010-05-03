class InsertionSort:
    def initialize(self, cmp, items):
        self.cmp = cmp
        self.items = items
        
    def sort(self): 
        yield
        for i in range(1, len(self.items.items)):
            j = i - 1
            while self.cmp.gtI(j, j+1) and self.cmp.gte(j, 0):
                self.items.swap(j, j+1)
                j -= 1
                yield
            yield