require 'colored_grid'
require 'aldous_border'

6.times do |n|
    grid = ColoredGrid.new(20,20)
    AldousBorder.on(grid)

    middle = grid[grid.rows / 2, grid.columns / 2]

    grid.distances = middle.distances

    filename = "aldous_border_%02d.png" % n
    grid.to_png.save(filename)
    puts "saved to #{filename}"

end
