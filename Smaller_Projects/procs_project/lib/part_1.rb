require "byebug"

def my_map(array, &prc)
    solution = []
    array.each { |ele| solution << prc.call(ele)}
    solution
end

def my_select(array, &prc)
    solution = []
    array.each { |ele| solution << ele if prc.call(ele) }
    solution 
end

def my_count(array, &prc)
    count = 0
    array.each { |ele| count += 1 if prc.call(ele) }
    count
end  

def my_any?(array, &prc)
    array.each { |ele| return true if prc.call(ele)}
    return false
end

def my_all?(array, &prc)
    array.each { |ele| return false if !(prc.call(ele))}
    return true
end

def my_none?(array, &prc)
    array.each { |ele| return false if prc.call(ele) }
    return true
end