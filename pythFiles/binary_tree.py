class BinaryTree:

    def on(self, grid):
        for grid.each_cell in cell:
            neighbors = []

            if cell.north is not None:
                neighbors.append(cell.north)
            if cell.east is not None:
                neighbors.append(cell.east)
            index = random.randint(0,list.count(neighbors))
            neighbor = neighbors.pop(index)

            cell.link(neighbor)
        return grid

