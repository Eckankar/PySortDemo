from Orderable import Orderable
from Comparator import Comparator
import pygame
from sys import exit
from threading import Event, Thread
from Algorithms import *
from optparse import OptionParser
from time import sleep

class SortDisplay:
    numLines = 150
    width = 400

    def __init__(self, algorithm, stopEvent):
        self.stopEvent = stopEvent
        
        self.items = Orderable(self.numLines)
        self.cmp = Comparator(self.items)
        
        algorithm.initialize(self.cmp, self.items)
        
        self.gen = algorithm.sort()

        pygame.init()
        self.window = pygame.display.set_mode((self.width, 5 * self.numLines))

        self.i = 0
        self.update()

    def update(self):
        self.window.fill((255, 255, 255))
        for i in range(0, len(self.items.items)):
            y = 5*(i+1)
            pygame.draw.line(self.window, (0, 0, 0), (3, y), ((self.width-6) * self.items.items[i] + 3, y))
        pygame.display.flip()
        try:
            self.gen.next()
        except StopIteration:
            self.stopEvent.set()
            

def main():
    parser = OptionParser()
    parser.add_option('-a', '--algorithm', type='string',
                      default='insertion', dest='algorithm',
                      help='algorithm to use')
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
        while True:
            stopEvent.wait(0.005)
            if stopEvent.isSet():
                break
            disp.update()
            
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

