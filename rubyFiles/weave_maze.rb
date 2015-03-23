require 'weave_grid'
require 'recursive_backtracker'

grid = WeaveGrid.new(20,20)
RecursiveBacktracker.on(grid)

filename = 'weave.png'
grid.to_png.save(filename)
puts "saved to #{filename}"
