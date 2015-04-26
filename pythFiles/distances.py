class Distances:

    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0

    def __getitem__(self, pos):
        return self.cells[pos]

    #set value
    def __setitem__(self, pos, val):
        self.cells[pos] = val

    #get keys of array
    def things(self):
        [cell for cell in self.cells]

    def keyExists(self, key):
        return key in self.cells

    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break
        return breadcrumbs

