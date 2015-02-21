class Cell

    attr_reader :row, :column
    attr_accessor :north, :south, :east, :west

    #constructor
    def initialize(row, column)
        @row, @column = row, column
        @links = {}
    end

    #links two cells
    def link(cell, bidi=true)
        @links[cell] = true
        cell.link(self, false) if bidi
        self
    end

    #unlinks two cells
    def unlink(cell, bidi=true)
        @links.delete(cell)
        cell.unlink(self, false) if bidi
        self
    end

    #gets all cells linked to this one
    def links
        @links.keys
    end

    #sees if cell is linked to another cell
    def linked?(cell)
        @linke.key?(cell)
    end

    def neighbrs
        list = []
        list << north if north
        list << south if south
        list << east if east
        list << west if west
    end

end
