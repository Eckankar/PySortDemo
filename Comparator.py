class Comparator:
    def __init__(self, items):
        self.comparisons = 0
        self.items = items

    def gtI(self, n, m):
        self.comparisons += 1
        return self.items.items[n] > self.items.items[m]

    def ltI(self, n, m):
        return self.gtI(m, n)

    def eqI(self, n, m):
        self.comparisons += 1
        return self.items.items[n] == self.items.items[m]

    def gteI(self, n, m):
        return not self.ltI(n, m)

    def lteI(self, n, m):
        return not self.gtI(n, m)
        
    ###############################
    
    def gt(self, n, m):
        self.comparisons += 1
        return n > m

    def lt(self, n, m):
        return self.gt(m, n)

    def eq(self, n, m):
        self.comparisons += 1
        return n == m

    def gte(self, n, m):
        return not self.lt(n, m)

    def lte(self, n, m):
        return not self.gt(n, m)
