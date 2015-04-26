from cell import Cell
import Image, ImageDraw

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = self.prepare_grid()
        self.configure_cells()
    
    def prepare_grid(self):
        grid = []
        for i in range(self.rows):
            currRow = []
            for j in range(self.columns):
                newCell = Cell(i,j)
                currRow.append( newCell )
            grid.append(currRow)
        return grid

    def configure_cells(self):
        c = len(self.grid)
        for cell in self.each_cell:
            row = cell.row
            col = cell.column

            cell.north = self[row-1, col]
            cell.south = self[row+1, col]
            cell.west = self[row, col-1]
            cell.east = self[row, col+1]

    def __getitem__(self, pos):
        x,y = pos
        if x < 0 or x >= self.rows:
            return None
        if y < 0 or y >= self.columns:
            return None
        return self.grid[x][y]

    def random_cell(self):
        row = random.randint(0,self.row)
        col = random.randint(0,list.count(self[row]))
        self[row,col]

    def size(self):
        return self.rows * self.columns

    @property
    def each_row(self):
        return [lst
                for lst in self.grid] 

    @property
    def each_cell(self):
        return [element
                for lst in self.grid
                for element in lst] 

    def contents_of(self, cell):
        return "   "

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        top = "|"
        bottom = "+"
        corner = "+"
        endRow = []
        for row in self.each_row:
            topRow = []
            botRow = []
            topRow.append(top)
            botRow.append(corner)
            for cell in row:
                body = self.contents_of(cell)
                if len(body) == 1:
                    body = " "+body+" "
                elif len(body) == 2:
                    body = " "+body
                topRow.append(body)
                if cell.is_linked(cell.east):
                    east_boundary = " "
                else:
                    east_boundary = "|"
                topRow.append(east_boundary)
                if cell.is_linked(cell.south):
                    south_boundary = "   "
                else:
                    south_boundary = "---"
                botRow.append(south_boundary)
                botRow.append(corner)
            endRow.append(''.join(topRow)+"\n"+''.join(botRow)+"\n")
        return output+''.join(endRow)

    def to_png(self,cell_size=10):
        img_width = cell_size*self.columns
        img_height = cell_size*self.rows

        background = 'white'
        wall = 'black'

        img = Image.new('RGB', (img_height+7, img_width+7), background)
        drawImg = ImageDraw.Draw(img)
        for cell in self.each_cell:
            x1 = cell.column*cell_size+3
            y1 = cell.row*cell_size+3
            x2 = (cell.column+1)*cell_size+3
            y2 = (cell.row+1)*cell_size+3

            if cell.north is None:
                drawImg.line( [x1, y1, x2, y1], wall)
            if cell.west is None:
                drawImg.line( [x1, y1, x1, y2], wall)
            if cell.is_linked(cell.east) == False:
                drawImg.line( [x2, y1, x2, y2], wall)
            if cell.is_linked(cell.south) == False:
                drawImg.line( [x1, y2, x2, y2], wall)
        return img


