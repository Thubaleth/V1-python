# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

# Example:
# make_acronym("New York") -> 'NY'
# make_acronym("same stuff different day") -> 'SSDD'
# make_acronym("Laugh out loud") -> 'LOL'
# make_acronym("don't over think stuff") -> 'DOTS'

def make_acronym(sentence):
    list_sentence = sentence.split()
    acronym = ""
    
    for i in list_sentence:
        acronym +=i[0].upper()
        
      
    return acronym

 

print(make_acronym("same stuff different day"))

#=========================================================================================
# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

# Example:
# reverse_array(["zero", "one", "two", "three"]) -> ['three', 'two', 'one', 'zero']
# reverse_array([7, 1, 8]) -> [8, 1, 7]


def reverse_array(arr):
    arr.reverse()
    return arr

print(reverse_array(["zero", "one", "two", "three"]))

#============================================================================================
# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

# Example:
# your_average_function([5, 2, 7, 24]) -> 9.5
# your_average_function([100, 6]) -> 53
# your_average_function([31, 32, 40, 12, 33]) -> 29.6
# your_average_function([]) -> None


def your_average_function(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count +=1

    if len(numbers) == 0:
        return None
    else:
        return total/count
    
print(your_average_function([]))


#=========================================================================================
# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

# Example:
# choose_divisibles([40, 7, 22, 20, 24], 4) -> [40, 20, 24]
# choose_divisibles([9, 33, 8, 17], 3) -> [9, 33]
# choose_divisibles([4, 25, 1000], 10) -> [1000]

def choose_divisibles(numbers, target):
    new_list = []
    for number in numbers:

        if number % target == 0:
            new_list.append(number)
        
    return new_list


print(choose_divisibles([9, 33, 8, 17], 3))