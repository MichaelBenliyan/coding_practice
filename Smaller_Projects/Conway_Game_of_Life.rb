def main 
    grid = Array.new(10) {Array.new(10, 0)}
    spawn(grid)
    print_grid(grid) 
    while true
        puts
        print "n for next or any char to stop"
        if gets.chomp == "n"
            new_grid = Array.new(10) {Array.new(10, 0)}    
            for x in 1..8
                for y in 1..8
                    new_grid[x][y] = get_new_state([x, y], grid)
                end
            end
            grid = new_grid
            print_grid(grid)
        else 
            return false
        end
    end
end
def get_new_state(cell, grid)
    if grid[cell[0]][cell[1]] == 1 && (surrounding_check(cell, grid) == 2 || surrounding_check(cell, grid) == 3)
        return 1 
    elsif grid[cell[0]][cell[1]] == 0 && surrounding_check(cell, grid) == 3
        return 1 
    else
        return 0
    end
end

def surrounding_check(cell, grid) #cell = [r, c]
    r = cell[0]
    c = cell[1]
    count = 0
    (-1..1).each do |r_delta|
        (-1..1).each do |c_delta|
            count += grid[r+r_delta][c+c_delta]
        end
    end
    count - grid[cell[0]][cell[1]]
end

def spawn(grid)
    max_spawn = grid.length*grid.length/5
    spawns = Hash.new(0)
    while spawns.keys.length < max_spawn 
        r = rand(1..8)
        c = rand(1..8)
        spawns[[r, c]] += 1 
    end
    spawns.keys.each { |pair| grid[pair[0]][pair[1]] = 1}
end

def print_grid(grid)
    for x in 1..8
        print grid[x][1..-2]
        puts
    end
end

main 


#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.
