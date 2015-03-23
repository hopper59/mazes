require 'triangle_grid'
require 'recursive_backtracker'

grid = TriangleGrid.new(10,17)
RecursiveBacktracker.on(grid)

filename = "delta.png"
grid.to_png.save(filename)
puts "saved to #{filename}"
