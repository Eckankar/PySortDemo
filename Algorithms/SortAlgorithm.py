class SortAlgorithm:
    """
    Base class to be used for sorting algorithms.

    An algorithm must be initialized with initialize before use.

    The field 'cmp' contains a Comparator to be used for comparison in the
    algorithm. Please use this for comparisons, as we wish to count these.

    The field 'items' contains a Orderable containing the items to be sorted.
    Note that you should prefer using the 'swap' method from this class for
    swapping elements, as we wish to count these.
    
    The field 'markers' contains a Markers that can be used for illustrative
    purposes.
    """

    def initialize(self, cmp, items, markers):
        """ Basic initialization of algorithm before use. """
        self.cmp = cmp
        self.items = items
        self.markers = markers

    def sort(self):
        """
        Does the actual sorting.

        Should be implemented as a generator function, that is, it should yield
        execution after each significant step in its execution, to allow for
        redrawing of the display, as well as slowing down the execution for
        better visual effect.

        In addition, the algorithm should yield before doing anything, to allow
        for initial drawing of the unsorted lines.
        """
        pass
