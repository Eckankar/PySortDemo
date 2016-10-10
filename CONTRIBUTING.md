# Contributing to PySortDemo

## Getting your environment set up

See [README](https://github.com/Eckankar/PySortDemo/blob/master/README) for instructions on how to run the software.

## Contributing a sorting algorithm

This is first and foremost a visualization project, i.e. a project focused on providing a visualization of how sorting algorithms work for students and other interested parties. Because of this, you not only have to implement a given algorithm, but also decide on how to illustrate key concepts.

For inspiration on the currently available sorting algorithms, take a look at the [Algorithms](https://github.com/Eckankar/PySortDemo/tree/master/Algorithms) directory. [GnomeSort](https://github.com/Eckankar/PySortDemo/blob/master/Algorithms/GnomeSort.py) is a simple example of a sorting algorithm, with simple visualization due to the nature of the algorithm. [Quicksort](https://github.com/Eckankar/PySortDemo/blob/master/Algorithms/QuickSort.py) is a more involved visualization; showing the splits performed in running the algorithm.

### Practicalities

Algorithm implementations must subclass from [SortAlgorithm](https://github.com/Eckankar/PySortDemo/blob/master/Algorithms/SortAlgorithm.py). The items you wish to sort are available in `self.items`, however, you should rarely need to access them directly. You will also need to add the algorithm to the algorithm list in [SortDisplay.py](https://github.com/Eckankar/PySortDemo/blob/master/SortDisplay.py).

All comparisons must use `self.cmp`, which is an instance of [Comparator](https://github.com/Eckankar/PySortDemo/blob/master/Comparator.py) and has the most common comparison operations available. Examples: If you want to say `self.items[i] > 0`, instead say `self.cmp.gt(self.items[i], 0)`. If you want to say `self.items[i] >= self.items[j]`, instead say `self.cmp.gteI(i, j)`. See the Comparator module for documentation of the available comparison operations.

To draw colored lines for illustration, use `self.markers`, which is an instance of [Markers](https://github.com/Eckankar/PySortDemo/blob/master/Markers.py). See the module for documentation.

When creating a marker, you can either decide to change the color of an element (`above` set to `False`; for instance used for highlighting the current element you're looking at), or draw a separator line above an element (`above` set to `True`; for instance used to show that the problem has been split into smaller sub-problems). The return value of `addMarker` is needed for later manipulation of the marker, so keep track of that.

The algorithms are implemeted as iterators, as this allows the program to step through the algorithm at it's own pace, allowing for the simulation to be slowed down. This is done by having the sorting function yield whenever a logical step has occurred in the algorithm. See the other algorithms for examples.
