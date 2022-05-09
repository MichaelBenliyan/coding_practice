# require "byebug"
class Board
    attr_reader :size, :grid
    def initialize(number)
        @grid = Array.new(number) {Array.new(number, "?")}
        @size = number * number
        @number = number
    end

    def [](coordinates)
        return nil if @grid[coordinates[0]] == nil
        @grid[coordinates[0]][coordinates[1]]
    end

    def []= (coordinates, value) 
        @grid[coordinates[0]][coordinates[1]] = value
    end

    def num_ships
        count = 0
        @grid.each do |array|
            array.each { |location| count += 1 if location == :S }
        end
        count
    end

    def attack(position)
        r = position[0]
        c = position[1]
        if self[position] == :S 
            self[position] = :H 
            # if r > 0 && c > 0 && r < @number - 1
            #     if @grid[r+1][c] != :S && @grid[r-1][c] != :S && @grid[r][c+1] != :S && self[r][c-1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # elsif r > 0 && c > 0 && r == @number - 1
            #     if @grid[r-1][c] != :S && @grid[r][c+1] != :S && self[r][c-1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # elsif r == 0 && c > 0 
            #     if @grid[r+1][c] != :S && @grid[r][c+1] != :S && self[r][c-1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # elsif r > 0 && c == 0 && r < @number - 1
            #     if @grid[r+1][c] != :S && @grid[r-1][c] != :S && @grid[r][c+1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # elsif r > 0 && c == 0 && r == @number - 1
            #     if @grid[r-1][c] != :S && @grid[r][c+1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # elsif r == 0 && c == 0 
            #     if @grid[r+1][c] != :S && @grid[r][c+1] != :S
            #         puts "You sunk my battleship!"
            #     end
            # end
            return true
        else
            self[position] = "-" 
            return false
        end
    end

    def place_random_ships
        num_battleships = @number/2
        hash = Hash.new { |h, k| h[k] = []}
        while hash.keys.length < num_battleships
            row = rand(0..(@number-1))
            column = rand(0..(@number-1))
            direction = rand(1..2) #1 => down, 2 => right
            ship_length = rand(2..5)
            start_position = [row, column]
            
            if check_buffer(row, column, direction, ship_length) && check_path(row, column, direction, ship_length)
                hash[start_position] << direction
                hash[start_position] << ship_length
            end
            hash.each { |pos, v| boat_placer(pos, v) }
        end
        # puts hash.keys
    end

    def boat_placer(pos, array)
        r = pos[0]
        c = pos[1]
        direction = array[0]
        ship_length = array[1]
        if direction == 1 #down
            (0...(ship_length)).each { |i| @grid[r+i][c] = :S}
        elsif direction == 2 #right
            (0...(ship_length)).each { |i| @grid[r][c+i] = :S}
        end
    end

    #Original Version: 
    # def place_random_ships
    #     num_battleships = @size/4
    #     hash = Hash.new(0)
    #     while hash.keys.length < num_battleships do 
    #         row = rand(0..(@number-1))
    #         column = rand(0..(@number-1))
    #         position = [row, column]
    #         hash[position] += 1
    #     end
    #     hash.keys.each { |k| self[k] = :S }
    # end

    def hidden_ships_grid
        dup_grid = [] 
        @grid.map { |array| dup_grid << array.dup }
        dup_grid.each do |array|
            array.each.with_index do |ele, i| 
                if ele == :S
                    array[i] = "?"
                end
            end
        end
        dup_grid
    end

    def self.print_grid(grid)
        grid.each do |array| 
            puts array.join(" ")
        end
    end 

    def cheat 
        Board.print_grid(@grid)
    end
    
    def print
        Board.print_grid(self.hidden_ships_grid)
    end



    def check_path(row, column, direction, ship_length) # 0 < direction <= 4
        #debugger
        check_list = []
        if direction == 1 #down
            (0..(ship_length-1)).each { |i| check_list << [row + i, column]}
            return check_list.all? { |pos| self[pos] == "?"}
        elsif direction == 2 #right
            (0..(ship_length-1)).each { |i| check_list << [row, column + i]}
            return check_list.all? { |pos| self[pos] == "?"}
        end
        false
    end

    def check_buffer(row, column, direction, ship_length)
        buffer_size = ((ship_length + 2) * 3) - ship_length
        check_list = []
        if direction == 1 #down
            r = row - 1
            c = column
            [-1, 1].each do |delta|
                i = 0 
                side = c + delta
                while i < ship_length + 2
                    check_list << [r+i, side]
                    i += 1 
                end
            end
            i = 0 
            while i <= ship_length
                check_list << [r+i, c]
                i += ship_length
            end
            return check_list.all? { |pos| self[pos] == "?" || self[pos] == nil}
        elsif direction == 2 # right
            r = row 
            c = column - 1 
            [-1, 1]. each do |delta|
                i = 0 
                side = r + delta
                while i < ship_length + 2
                    check_list << [side, c+i]
                    i += 1 
                end
            end
            i = 0 
            while i <= ship_length
                check_list << [r+i, c]
                i += ship_length
            end
            return check_list.all? { |pos| self[pos] == "?" || self[pos] == nil}
        end
    end
end

# board = Board.new(4)
# board.place_random_ships()
# board.grid.each do |array| 
#     print array
#     puts
# end


