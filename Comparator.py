class Comparator:
    """
    Comparator class; serves the purpose of keeping track of how many comparisons an algorithm makes.

    The methods are named as follows:
    gt - greater than - >
    gte - greater than or equal to - >=
    lt - less than - <
    lte - less than or equal to - <=
    eq - equal to - ==
    
    There are two versions of each method; one with I appended to the end and one without it. (gtI vs gt)
    The one with the I appended compares on the items to be sorted, while the ones without compare the passed arguments.
    For instance, gtI(4, 5) compares element 4 with element 5, while gt(4, 5) is equivalent to 4 > 5.

    The comparison count is available in the field 'comparisons'.
    """

    def __init__(self, items):
        self.comparisons = 0
        self.items = items

    ###############################
    # Element comparators
    ###############################

    def gtI(self, n, m):
        """ items[n] > items[m] """
        self.comparisons += 1
        return self.items.items[n] > self.items.items[m]

    def ltI(self, n, m):
        """ items[n] < items[m] """
        return self.gtI(m, n)

    def eqI(self, n, m):
        """ items[n] == items[m] """
        self.comparisons += 1
        return self.items.items[n] == self.items.items[m]

    def gteI(self, n, m):
        """ items[n] >= items[m] """
        return not self.ltI(n, m)

    def lteI(self, n, m):
        """ items[n] <= items[m] """
        return not self.gtI(n, m)

    ###############################
    # Value comparators
    ###############################

    def gt(self, n, m):
        """ n > m """
        self.comparisons += 1
        return n > m

    def lt(self, n, m):
        """ n < m """
        return self.gt(m, n)

    def eq(self, n, m):
        """ n == m """
        self.comparisons += 1
        return n == m

    def gte(self, n, m):
        """ n >= m """
        return not self.lt(n, m)

    def lte(self, n, m):
        """ n <= m """
        return not self.gt(n, m)
