# Write a function `divisible_range(min_val, max_val, num)` that prints all numbers
# between min_val and max_val (exclusive) that are divisible by num.
# The function does not return a value, just prints.

# Example:
#divisible_range(17, 40, 9)
# 18
# 27
# 36

#divisible_range(10, 24, 4)
# 12
# 16
# 20


def divisible_range(min_val,max_val,num):

    for i in range(min_val,max_val+1):
        if i % num == 0 or i % num == 0:
            print(i)



divisible_range(17, 40, 9)



# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

# Example:
#reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

#reverse_iterate("box")
# x
# o
# b

def reverse_iterate(text):
    for i in range(len(text) - 1, -1, -1):
        print(text[i])

reverse_iterate("carrot")