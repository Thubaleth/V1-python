# Write a function `pair_print(arr)` that accepts a list and prints all unique pairs
# of elements in the list. It doesn't need to return anything.

# Example:
#pair_print(["artichoke", "broccoli", "carrot", "daikon"])
# prints
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon

def pair_print(arr):
   for i in range(len(arr)):
       for x in range(i+1,len(arr)):
           print(f'{arr[i]} -{arr[x]}')

pair_print(["artichoke", "broccoli", "carrot", "daikon"])
       

#=========================================================================================
# Write a function `print_combinations(arr1, arr2)` that accepts two lists.
# The function should print all combinations taking one element from the first list
# and one from the second list. It doesn't need to return anything.

# Example:
#colors = ["gray", "cream", "cyan"]
#clothes = ["shirt", "flannel"]
#print_combinations(colors, clothes)
# prints:
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel

def print_combinations(arr1, arr2):
    for i in arr1:
        for x in arr2:
            print(f'{i}  {x}')

colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)


# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

# Example:
#two_sum([2, 3, 5, 9], 7) #-> True
#two_sum([2, 3, 5, 9], 4) #-> False
#two_sum([6, 3, 4], 10) #-> True
#two_sum([6, 5, 1], 10) #-> False

def two_sum(numbers, target):
    
    for j in range(len(numbers)) :
        for i in range(j+1,len(numbers)):

            if numbers[i] + numbers[j] == target:
                return True
    
    return False
            


print( two_sum([6, 3, 4], 10)  )
        


