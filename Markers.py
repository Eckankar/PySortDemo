class Markers:
    """
    Keeps track of markers (colored lines) we want to display to make the
    visualizations more appealing.
    """
    def __init__(self):
        self.markers = {}
        self.id = 0

    def addMarker(self, above, index, color):
        """
        Adds a marker to our collection.
        
        Parameters:
        - above (boolean): If true, the marker will be displayed above the line of the given index.
                           If false, the marker will be displayed on the line of the given index.
        - index (int): Index of the marker the marker should be displayed near.
        - color (color): The color the marker is to have on the display.
                         Should be passed as a RGB-tuple; e.g. (255, 0, 0) = red.

        Returns an the id of the marker created, to be used for modifying/removing the marker at a later point in time.
        """
        self.id += 1

        marker = { 'id': self.id,
                   'above': above,
                   'index': index,
                   'color': color }

        self.markers[self.id] = marker

        return self.id

    def moveMarker(self, id, index):
        """ Moves the marker with the given id to the given index. """
        self.markers[id]['index'] = index

    def removeMarker(self, id):
        """ Removes the marker with the given id. """
        del self.markers[id]


