require 'grid'

require 'recursive_backtracker'

grid = Grid.new(5,5)

#orphan cell in northwest corner..
grid[0,0].east.west = nil
grid[0,0].south.north = nil

#and southeast corner
grid[4,4].west.east = nil
grid[4,4].north.south = nil

RecursiveBacktracker.on(grid, grid[1,1])
puts grid
