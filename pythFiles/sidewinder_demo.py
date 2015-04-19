from sidewinder import Sidewinder
from grid import Grid

grid = Grid(4,4)
side = Sidewinder()
side.on(grid)
#print grid
img = grid.to_png(10)
fileName = "maze.png"
img.save(fileName, "PNG")
