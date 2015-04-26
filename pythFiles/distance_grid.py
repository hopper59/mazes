from grid import Grid

class DistanceGrid(Grid):

    def __inti__(sef):
        self.distances = []
    
    #todo fix this
    def contents_of(self, cell):
        if self.distances and self.distances.keyExists(cell):
            return chr(self.distances[cell]+97)
        else:
            super

