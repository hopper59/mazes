from cell import Cell

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = self.prepare_grid()
        print '{0}'.format(len(self.grid))
        self.configure_cells()
    
    def prepare_grid(self):
        grid = []
        for i in range(self.rows):
            currRow = []
            for j in range(self.columns):
                newCell = Cell(i,j)
                print 'new cell {0},{1}'.format(i,j)
                currRow.append( newCell )
            grid.append(currRow)
        return grid

    def configure_cells(self):
        c = list.count(self.grid)
        print '{0}'.format(self.rows)
        return
        for cell in self.each_cell:
            row = cell.row
            col = cell.col

            cell.north = self[row-1, col]
            cell.south = self[row+1, col]
            cell.west = self[row, col-1]
            cell.east = self[row, col+1]

    def __getitem__(self, pos):
        x,y = pos
        if (x < 0 or x > self.rows):
            return None
        if (y < 0 or y > list.count(self[x])):
            return None
        return self.grid[x,y]

    def random_cell(self):
        row = random.randint(0,self.row)
        col = random.randint(0,list.count(self[row]))
        self[row,col]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        rows = []
        for row in range(list.count(self.grid)):
            rows.append(row)
            print '1'
        return rows

    def each_cell(self):
        cells = []
        for row in each_row:
            for row in cell:
                cells.append(cell)
                print '{0}{1}'.format(cell.row,cell.column)
        return cells

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        return
        for row in self.each_row:
            top = "|"
            bottom = "+"
            for cell in row:
                body = "   " 
                if cell.is_linked(cell.east):
                    east_boundary = " "
                else:
                    east_boundary = "|"
                if cell.is_linked(cell.south):
                    south_boundary = "   "
                else:
                    south_boundary = "---"
                corner = "+"
            print '{0}{1}{2}'.format(top,body,east_boundary)
            print '{0}{1}{2}'.format(bottom,south_boundary,corner)

