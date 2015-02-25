require 'grid'
require 'aldous_border'

grid = Grid.new(20,20)
AldousBorder.on(grid)

filename = 'aldous_border.png'
grid.to_png.save(filename)
puts "saved to #{filename}"
