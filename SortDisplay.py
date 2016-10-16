#!/usr/bin/env python2
from Orderable import Orderable
from Comparator import Comparator
from Markers import Markers
import pygame
from threading import Event, Thread
from Algorithms import *
from optparse import OptionParser
from time import sleep
import copy


class SortDisplay:
    """Visualization of sorting algorithms."""
    def __init__(self, algorithm, stop_event, options, compare=None):
        self.stopEvent = stop_event

        self.numLines = options.numLines
        self.width = options.width

        self.compare = compare

        self.stop = False
        self.cstop = compare is None
        self.items = Orderable(self.numLines)
        self.cmp = Comparator(self.items)
        self.markers = Markers()

        algorithm.initialize(self.cmp, self.items, self.markers)

        self.gen = algorithm.sort()

        if compare is not None:
            self.citems = copy.deepcopy(self.items)
            self.ccmp = Comparator(self.citems)
            self.cmarkers = Markers()
            compare.initialize(self.ccmp, self.citems, self.cmarkers)

            self.cgen = compare.sort()

        pygame.init()

        if compare is None:
            self.window = pygame.display.set_mode((self.width, 6 * (self.numLines+1)))
        else:
            self.window = pygame.display.set_mode((self.width * 2 + 5, 6 * (self.numLines+1)))

        self.i = 0
        self.update()

    def update(self):
        """ Update the graphical display. """
        self.window.fill((255, 255, 255))

        self.__update_algorithm(self.items.items, self.markers.markers, 0)

        if self.compare is not None:
            self.__update_algorithm(self.citems.items, self.cmarkers.markers, self.width + 5)

        pygame.display.flip()

    def __update_algorithm(self, items, markers, xoffset=0):
        for i in range(0, len(items)):
            y = 6 * (i+1)
            pygame.draw.line(self.window, (0, 0, 0), (3 + xoffset, y),
                             ((self.width-6) * items[i] + 3 + xoffset, y))

        for id, marker in markers.iteritems():
            y = 6 * (marker['index'] + 1)

            if marker['above']:
                y -= 3
                xStart = 2
                xEnd = self.width - 2
            else:
                xStart = 3
                try:
                    xEnd = (self.width - 6) * items[marker['index']] + 3
                except:
                    xEnd = 3

            pygame.draw.line(self.window, marker['color'],
                             (xStart + xoffset, y), (xEnd + xoffset, y))

    def step(self):
        try:
            self.gen.next()
        except StopIteration:
            self.stop = True

        if self.compare is not None:
            try:
                self.cgen.next()
            except StopIteration:
                self.cstop = True

        if self.stop and self.cstop:
            self.stopEvent.set()


def main():
    """ Main method, called on execution of the .py from the commandline """
    algorithms = {
            'insertionsort'       : InsertionSort(),
            'quicksort'           : QuickSort(),
            'selectionsort'       : SelectionSort(),
            'mergesort'           : MergeSort(),
            'runsort'             : RunSort(),
            'patiencesort'        : PatienceSort(),
            'introsort'           : IntroSort(),
            'bubblesort'          : BubbleSort(),
            'cocktailsort'        : CocktailSort(),
            'shellsort'           : ShellSort(),
            'heapsort'            : HeapSort(),
            'insertionquicksort'  : InsertionQuickSort(),
            'insertionmergesort'  : InsertionMergeSort(),
            'oddevensort'         : OddEvenSort(),
            'gnomesort'           : GnomeSort(),
            'binaryinsertionsort' : BinaryInsertionSort(),
            'bidirselectionsort'  : BidirectionalSelectionSort(),
            'stoogesort'          : StoogeSort(),
            'sillysort'           : SillySort(),
            'bogosort'            : BogoSort(),
            'combsort'            : CombSort(),
            'inplacemergesort'    : InplaceMergeSort(),
            'jsort'               : JSort(),
    }
    parser = OptionParser()
    parser.add_option('-a', '--algorithm', type='choice',
                      default='mergesort', dest='algorithm',
                      choices=algorithms.keys(),
                      help='algorithm to use')
    parser.add_option('-d', '--delay', type='float',
                      default=0.01, dest='delay',
                      help='delay between each step in seconds')
    parser.add_option('-w', '--width', type='int',
                      default=400, dest='width',
                      help='width of window')
    parser.add_option('-n', type='int',
                      default=100, dest='numLines',
                      help='number of lines to sort')
    parser.add_option('-c', type='choice', default=None,
                      dest='compare', choices=algorithms.keys(),
                      help='algorithm to compare with')
    (options, args) = parser.parse_args()
    algorithm = algorithms[options.algorithm]
    compare = None if options.compare is None else algorithms[options.compare]

    stopEvent = Event()

    disp = SortDisplay(algorithm, stopEvent, options, compare)

    def update():
        """ Update loop; updates the screen every few seconds. """
        while True:
            stopEvent.wait(options.delay)
            disp.update()
            if stopEvent.isSet():
                break
            disp.step()

    t = Thread(target=update)
    t.start()

    while not stopEvent.isSet():
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopEvent.set()
        except KeyboardInterrupt:
            stopEvent.set()

    print disp.items.swaps, "swaps"
    print disp.cmp.comparisons, "comparisons"
    if compare is not None:
        print "comparison:"
        print disp.citems.swaps, "swaps"
        print disp.ccmp.comparisons, "comparisons"

if __name__ == "__main__":
    main()
