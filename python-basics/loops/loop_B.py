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
