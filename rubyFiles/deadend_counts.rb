require 'grid'

require 'binary_tree'
require 'sidewinder'
require 'aldous_border'
require 'wilsons'
require 'hunt_and_kill'

algorithms = [BinaryTree, Sidewinder, AldousBorder, Wilsons, HuntAndKill]

tries = 100
size = 20
averages = {}

algorithms.each do |algorithm|
    puts "running #{algorithm}..."

    deadend_counts = []
    tries.times do
        grid = Grid.new(size, size)
        algorithm.on(grid)
        deadend_counts << grid.deadends.count
    end

    total_deadends = deadend_counts.inject(0) { |s,a| s + a }
    averages[algorithm] = total_deadends / deadend_counts.length
end

total_cells = size * size
puts "\nAverage dead-ends per #{size}x#{size} maze(#{total_cells} cells):\n\n"

sorted_algorithms = algorithms.sort_by { |algo| -averages[algo] }

sorted_algorithms.each do |algo|
    percentage = averages[algo] * 100.0 / (size * size)
    puts "%14s : %3d/%d (%d%%)" % 
        [algo, averages[algo], total_cells, percentage]
end


