require "byebug"

def reverser(string, &prc)
    prc.call(string.reverse)
end

def word_changer(sentence, &prc)
    words = []
    sentence.split(" ").each { |word| new_sentence << prc.call(word)}
    words.join(" ")
end

def greater_proc_value(num, prc1, prc2)
    res1 = prc1.call(num)
    res2 = prc2.call(num)
    [res1, res2].max
end

def and_selector(array, prc1, prc2)
    new_array = []
    array.each { |ele| new_array << ele if prc1.call(ele) && prc2.call(ele) }
    new_array
end

def alternating_mapper(array, prc1, prc2)
    new_array = []
    array.each.with_index do |ele, i|
        if i.even? 
            new_array << prc1.call(ele)
        else
            new_array << prc2.call(ele)
        end
    end
    new_array
end