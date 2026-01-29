
#=============================================================================================
# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.
def print2d(matrix):

    for i in matrix:
        for j in i:
            print(j)

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
    
print(make_matrix(3, 5, None))