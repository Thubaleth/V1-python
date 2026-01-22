# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

# Example:
#total([3, 2, 8]) #-> 13
#total([-5, 7, 4, 6]) #-> 12
#total([7]) #-> 7
#total([]) #-> 0


def total(numbers):
    sum = 0
    for i in numbers:
        sum += i
    
    return sum

print(total([3, 2, 8]))


#===========================================================================================

# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

# Example:
#stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
#stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
#stay_positive([-11, -30]) #-> []

def stay_positive(numbers):
   positive = []

   for  number in numbers:
        
        if number > 0:
           positive.append(number)
    
   return positive
           
print(stay_positive([10, -4, 3, 6]))


#=========================================================================================

# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

# Example:
#bleep_vowels("skateboard") #-> 'sk*t*b**rd'
#bleep_vowels("slipper") #-> 'sl*pp*r'
#bleep_vowels("range") #-> 'r*ng*'
#leep_vowels("brisk morning") #-> 'br*sk m*rn*ng'


def bleep_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    for char in text:
        if char in vowels:
            result += '*'
        else:
            result += char

    return result


print(bleep_vowels("skateboard"))   # sk*t*b**rd


#===================================================================

# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

# Example:
#filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
#filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']

def filter_long_words(words):
    new_words = []

    for i in words:
        if len(i) < 5:
            new_words.append(i)

    return new_words

print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))


    
  
        
    #===========================================================================
    # Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

# Example:
#num_odds([4, 7, 2, 5, 9]) #-> 3
#num_odds([11, 31, 58, 99, 21, 60]) #-> 4
#num_odds([100, 40, 4]) #-> 0


def num_odds(numbers):
    count = 0
    for number in numbers:

        if number % 2 == 1:
            count += 1
        
    return count


print(num_odds([11, 31, 58, 99, 21, 60]))


#===========================================================================
# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

# Example:
#strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
#strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]



def strings_to_lengths(strings):
    new_list = []

    for string in strings:

        new_list.append(len(string))
    
    return new_list

strings_to_lengths(["on", "off", "handmade"])


#================================================================================
# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

# Example:
#divisors(15) #-> [1, 3, 5, 15]
#divisors(7) #-> [1, 7]
#divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

# Write a function `divisors(num)` that accepts a number.

def divisors(num):
     

     div_list = []

     for i in range(1,num + 1):
          
          if num % i == 0:
              div_list.append(i)

     return div_list
             

print(divisors(15))
    


    
          
