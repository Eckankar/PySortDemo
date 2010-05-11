from SortAlgorithm import SortAlgorithm

class BidirectionalBubbleSort(SortAlgorithm):
    def sort(self): 
        yield
        goingDown = True
        changed = True
        p = 0        
        r = len(self.items.items)-1
        while p != r and changed:
            changed = False
            if goingDown:
                for i in range(p, r):
                    if self.cmp.gtI(i, i+1):
                        self.items.swap(i, i+1)
                        changed = True
                    yield
                r -= 1
            else:
                for i in range(r, p, -1):
                    if self.cmp.gtI(i-1, i):
                        self.items.swap(i-1, i)       
                        changed = True
                    yield
                p += 1
                
            goingDown = not goingDown
            yield
            
