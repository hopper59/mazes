import random

class Sidewinder:

    def on(self, grid):
        for row in grid.each_row:
            run = []
            for cell in row:
                run.append(cell)

                at_eastern_boundary = (cell.east is None)
                at_northern_boundary = (cell.north is None)

                should_close_out = at_eastern_boundary or (at_northern_boundary == False and random.randint(0,2) == 0)
                if should_close_out == True:
                    index = random.randint(0,len(run))
                    if index == len(run):
                        index = index - 1
                    member = run.pop(index)
                    if member.north is not None:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
        return grid



