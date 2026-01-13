def add(a,b):
    print(a+b)

add(3,2)


def greet():
    print("hey")
    print("programmers")

def whistle():
    print("doot")

print("first")
print("second")
greet()
print("third")
print("fourth")
whistle()

#=======================================

def how_many():
    return 42

print(how_many)
print(how_many())

the_answer = how_many()
print(the_answer)

def how_much():
    5   # does nothing

print(how_much())

# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.

def is_div_by_4(num):

    if num % 4 == 0:
        return True
    else:
        return False
    
print(is_div_by_4(8))   # True
print(is_div_by_4(12))  # True
print(is_div_by_4(24))  # True
print(is_div_by_4(9))   # False
print(is_div_by_4(10))  # False

# Write a function `keep_it_quiet` that accepts a string as an argument.
# The function should return the lowercase version of the string
# with 3 periods added to the end.

def keep_it_quiet(str):
    return str.lower()

print( keep_it_quiet("Hooray")+"...")

# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.

def is_long(str):
    if len(str) > 5:
       return True
    else:
       return False


print(is_long("pie"))         # False
print(is_long("kite"))        # False
print(is_long("kitty"))       # False
print(is_long("telescope"))   # True
print(is_long("thermometer")) # True
print(is_long("restaurant"))  # True

# Write a function `half` that accepts a number as an argument.
# The function should return half of the number.

def half(number):
    return number / 2


print(half(8))    # 4
print(half(15))   # 7.5
print(half(90))   # 45


# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".

def ends_with_t(str):
    if str[-1:] == "t":
        return True
    else:
      return False

print(ends_with_t("smart"))      # True
print(ends_with_t("racket"))     # True
print(ends_with_t("taco"))       # False
print(ends_with_t("boomerang"))  # False

# Write a function `average` that accepts three numbers as arguments.
# The function should return the average of the three numbers.

def average(n1,n2,n3):
    sum = n1+n2+n3
    return sum/3


print(average(3, 10, 8))    # 7
print(average(10, 5, 12))   # 9
print(average(6, 20, 40))   # 22