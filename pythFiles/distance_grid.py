from grid import Grid

class DistanceGrid(Grid):

    def __inti__(sef):
        self.distances = []
    
    def contents_of(self, cell):
        if self.distances and self.distances.keyExists(cell):
            return chr(self.distances[cell]+97)
        else:
            return super(DistanceGrid,self).contents_of(cell)

