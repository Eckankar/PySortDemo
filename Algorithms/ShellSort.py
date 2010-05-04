class ShellSort:
    def initialize(self, cmp, items):
        self.cmp = cmp
        self.items = items
        
    def sort(self): 
        yield
        hs = [1]
        h = 1
        while h*3 + 1 < len(self.items.items):
            h = h*3 + 1
            hs.append(h)
        hs.reverse()
        
        for s in hs:
            for i in range(0, len(self.items.items), s):
                min = i
                for j in range(i, len(self.items.items)):
                    if self.cmp.gtI(min, j):
                        min = j
                self.items.swap(i, min)
                yield
