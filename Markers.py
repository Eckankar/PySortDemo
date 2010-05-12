class Markers:
    def __init__(self):
        self.markers = {}
        self.id = 0

    def addMarker(self, above, index, color):
        self.id += 1

        marker = { 'id': self.id,
                   'above': above,
                   'index': index,
                   'color': color }

        self.markers[self.id] = marker

        return self.id

    def moveMarker(self, id, index):
        self.markers[id]['index'] = index

    def removeMarker(self, id):
        del self.markers[id]


