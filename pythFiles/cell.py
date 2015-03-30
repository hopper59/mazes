class Cell:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {} 
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self
    
    def unlink(self, cell, bidi=True):
        self.links.remove(cell)
        if bidi:
            cell.unlink(self, False)
        return self

    def links(self):
        return self.link.keys()

    def is_linked(self, cell):
        return cell in self.links

    def neighbors(self):
        neighbor = []
        if self.north is not None:
            neighbor.append(self.north)
        if self.south is not None:
            neighbor.append(self.south)
        if self.east is not None:
            neighbor.append(self.east)
        if self.west is not None:
            neighbor.append(self.west)

        return neighbor

