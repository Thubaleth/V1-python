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
    vowels = ['a','e','i','o','u']
    result = ""
    for i in text:

        if i in vowels:
            result += '*'
            
    
  
        
    
    

    

    
print(bleep_vowels("skateboard"))
    
          
