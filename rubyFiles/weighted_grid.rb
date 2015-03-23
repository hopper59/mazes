require 'grid'
require 'weighted_cell'
require 'chunky_png'

class WeightedGrid < Grid

    attr_reader :distances

    def distances=(distances)
        @distances = distances
        farthest, @maximum = distances.max
    end

    def prepare_grid
        Array.new(@rows) do |row|
            Array.new(@columns) do |col|
                WeightedCell.new(row, col)
            end
        end
    end

    def background_color_for(cell)
        if cell.weight > 1
            ChunkyPNG::Color.rgb(255,0,0)
        elsif @distances
            distance = @distances[cell] or return nil
            intensity = 64 + 191 * (@maximum - distance ) / @maximum
            ChunkyPNG::Color.rgb(intensity, intensity, 0)
        end
    end

end
