require 'grid'

class ColoredGrid < Grid
    def distances=(distances)
        @distances = distances
        farthest, @maximum = distances.max
    end

    def background_color_for(cell)
        distance = @distances[cell] or return nil
        intensity = 255*(@maximum - distance)/@maximum
        ChunkyPNG::Color.rgb(0, intensity, 0)
    end
end
