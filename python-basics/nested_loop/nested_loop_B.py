
#=============================================================================================
# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.
def print2d(matrix):

    for i in matrix:
        for j in i:
            print(j)

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.


#print(make_matrix(3, 5, None))
#print(make_matrix(4, 2, "x"))
#print(make_matrix(2, 2, 0))

def make_matrix(m, n, value):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(value)
        matrix.append(row)
    
    return matrix
    
print(make_matrix(4, 2, "x"))
#==========================================================
# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    product = 1
    for row in matrix:
        for num in row:
            product *= num
    return product

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))  # 360
print(total_product(array2))  # 288

