"""
Write a function `pick_primes` that accepts a list of numbers.

The function should return a **new list** containing **only the prime numbers** from the original list.

You may want to **reuse the `is_prime` function**.

"""
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True


def pick_primes(lst):
    new_list = []
    for num in lst:
        if is_prime(num) == True:
         new_list.append(num)
    
    return new_list
        
print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []