class Player

    def get_move
        print 'enter a position with coordinates separated with a space like `4 7`'
        puts
        coordinates = gets.chomp.split(" ")
        coordinates.each.with_index {|ele, i| coordinates[i]=ele.to_i}
        coordinates
    end
end
