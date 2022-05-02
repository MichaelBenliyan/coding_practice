# Monkey-Patch Ruby's existing Array class to add your own custom methods
require "Byebug"
class Array
    def span
        return (self.max - self.min) if self.length > 0 
        nil
    end

    def average
        return (self.sum / (self.length * 1.0)) if self.length > 0 
        nil
    end

    def median
        return nil if self.length == 0 
        duplicate = []
        self.each { |n| duplicate << n}

        sorted = false
        while sorted == false
            sorted = true 
            (0...duplicate.length-1).each do |i|
                if duplicate[i] > duplicate[i+1]
                    duplicate[i], duplicate [i+1] = duplicate[i+1], duplicate[i]
                    sorted = false
                end
            end
        end

        if duplicate.length.even?
            return (duplicate[duplicate.length/2] + duplicate[duplicate.length/2 - 1])/2.0
        else
            return duplicate[duplicate.length/2]
        end
    end

    def counts
        counter = Hash.new(0)
        self.each { |ele| counter[ele] += 1 }
        counter
    end

    def my_count(value)
        counter = self.counts
        counter[value]
    end

    def my_index(value)
        self.each.with_index { |ele, i| return i if ele == value}
        nil 
    end

    def my_uniq
        uniques = []
        self.each { |ele| uniques << ele if !(uniques.include?(ele))}
        uniques
    end

    def my_transpose
        transposed = []
        self.length.times { |t| transposed << [] }
        r = 0
        c = 0
        while c < self.length
            self[c].each do |ele|
                transposed[r][c]  = ele
                r += 1   
            end
            r = 0
            c += 1
        end
        transposed
    end


end

arr = [ [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9] ]

print arr.my_transpose # => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
