import random

class BinaryTree:

    def on(self, grid):
        for cell in grid.each_cell:
            neighbors = []

            if cell.north is not None:
                neighbors.append(cell.north)
            if cell.east is not None:
                neighbors.append(cell.east)
            length = len(neighbors)
            if length == 0:
                continue
            else:
                index = random.randint(0,length)
            if index == length:
                index = index -1
            neighbor = neighbors.pop(index)

            cell.link(neighbor)
        return grid

