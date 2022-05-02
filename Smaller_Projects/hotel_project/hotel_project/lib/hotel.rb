require_relative "room"

class Hotel
    def initialize(name, rooms_hash)
        @name = name 
        @rooms = {}
        rooms_hash.each_pair { |k, v| @rooms[k] = Room.new(v)}
    end

    def name 
        @name.split(' ').each {|word| word.capitalize!}.join(" ")
    end

    def rooms
        @rooms
    end

    def room_exists?(room_name)
        @rooms.has_key? (room_name)
    end

    def check_in(person, room_name)
        if room_exists?(room_name)
            if @rooms[room_name].add_occupant(person)
                print "check in successful"
            else 
                print "sorry, room is full"
            end
        else
            print "sorry, room does not exist"
        end
    end

    def has_vacancy?
        @rooms.any? { |k, v| !(v.full?)}
    end

    def list_rooms
        room_list = []
        @rooms.each_pair do |k, v| 
            room_details = ""
            room_details += k + ".*" + v.available_space.to_s
            room_list << room_details
        end
        room_list.each { |r| puts r}
    end
            

end

