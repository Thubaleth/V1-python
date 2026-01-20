# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.

# Example:

#five_multiples_of(7)

# 7
# 14
# 21
# 28
# 35

def five_multiples_of(num):
    for i in range(1,6):
        print(num*i)

five_multiples_of(7)
    
#=======================================================================================================

# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

# Example:
#sum_up_to(4)  #-> 10
#sum_up_to(5)  #-> 15
#sum_up_to(2)  #-> 3

def sum_up_to(max_num):
    total = 0
    for num in range(1, max_num + 1):
        total += num
    print(total)


sum_up_to(4)
#=================================================================================================

# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:
# no_ohs("code")
# c
# d
# e

def no_ohs(text):
    for i in range(len(text)):
        if text[i] == 'o':
            continue
        else:
        
         print(text[i])

no_ohs('codoe')


# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

# Example:
#odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
#odd_sum(5)  #-> 9   # 1 + 3 + 5

def odd_sum(max_num):
    sum = 0
    for i in range(1,max_num+1):
        if i % 2 == 1:
            sum += i

    return sum

print(odd_sum(10))


#========================================================================================
# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

# Example:
#string_repeater("q", 4)  #-> 'qqqq'
#string_repeater("go", 2) #-> 'gogo'
#string_repeater("tac", 3) #-> 'tactactac'

def string_repeater(text, n):
   print(text*n)

string_repeater("go",2)


#========================================================================================
# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

# Example:
#product_up_to(4) #-> 24
#product_up_to(5) #-> 120
#product_up_to(7) #-> 5040

def product_up_to(max_num):
    total = 1
    for i in range(1,max_num+1):
        total *= i

    return total

print(product_up_to(4))



#=============================================================================================

# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.

# Example:
#div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15


def div_by_either(num1, num2, max_num):
    for num in range(1, max_num):
        if num % num1 == 0 or num % num2 == 0:
            print(num)

div_by_either(4, 3, 16)


        
    















