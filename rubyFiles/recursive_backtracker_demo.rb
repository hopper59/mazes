require 'grid'
require 'recursive_backtracker'

grid = Grid.new(20,20)
RecursiveBacktracker.on(grid)
grid.braid(0.5)

filename = 'recursive_backtracker.png'
#grid.to_png.save(filename)
grid.to_png(10,0.1).save(filename)
puts "saved to #{filename}"
