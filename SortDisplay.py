#!/usr/bin/python
from Orderable import Orderable
from Comparator import Comparator
from Markers import Markers
import pygame
from threading import Event, Thread
from Algorithms import *
from optparse import OptionParser
from time import sleep

class SortDisplay:
    """Visualization of sorting algorithms."""

    numLines = 100
    width = 400

    def __init__(self, algorithm, stop_event):
        self.stopEvent = stop_event

        self.items = Orderable(self.numLines)
        self.cmp = Comparator(self.items)
        self.markers = Markers()

        algorithm.initialize(self.cmp, self.items, self.markers)

        self.gen = algorithm.sort()

        pygame.init()
        self.window = pygame.display.set_mode((self.width, 6 * (self.numLines+1)))

        self.i = 0
        self.update()

    def update(self):
        """ Update the graphical display. """
        self.window.fill((255, 255, 255))
        for i in range(0, len(self.items.items)):
            y = 6 * (i+1)
            pygame.draw.line(self.window, (0, 0, 0), (3, y),\
                             ((self.width-6) * self.items.items[i] + 3, y))

        for id, marker in self.markers.markers.iteritems():
            y = 6 * (marker['index'] + 1)

            if marker['above']:
                y -= 3
                xStart = 2
                xEnd = self.width - 2
            else:
                xStart = 3
                try:
                    xEnd = (self.width - 6) * self.items.items[marker['index']] + 3
                except:
                    xEnd = 3

            pygame.draw.line(self.window, marker['color'],\
                             (xStart, y), (xEnd, y))

        pygame.display.flip()

    def step(self):
        try:
            self.gen.next()
        except StopIteration:
            self.stopEvent.set()


def main():
    """ Main method, called on execution of the .py from the commandline """
    parser = OptionParser()
    parser.add_option('-a', '--algorithm', type='string',
                      default='insertion', dest='algorithm',
                      help='algorithm to use')
    parser.add_option('-d', '--delay', type='float',
                      default=0.01, dest='delay',
                      help='delay between each step in seconds')
    (options, args) = parser.parse_args()
    try:
        algorithm = {
            'insertionsort': InsertionSort(),
            'quicksort'    : QuickSort(),
            'selectionsort': SelectionSort(),
            'mergesort'    : MergeSort(),
            'bubblesort'   : BubbleSort(),
            'bibubblesort' : BidirectionalBubbleSort(),
            'shellsort'    : ShellSort(),
            'heapsort'     : HeapSort(),
        }[options.algorithm];
    except KeyError:
        algorithm = InsertionSort()

    stopEvent = Event()

    disp = SortDisplay(algorithm, stopEvent)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopEvent.set()

    print disp.items.swaps, "swaps"
    print disp.cmp.comparisons, "comparisons"

if __name__ == "__main__":
    main()

