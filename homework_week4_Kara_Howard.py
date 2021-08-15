"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

EXAMPLE OUTPUT

result = [3,3]

"""

def main():
    pass

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

def search_in_matrix(matrix, target):

    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            
            element = matrix[i][j]
            if element == target:
                return f'The target is at position {[i,j]} in the matrix.'
    return [-1, -1]
            
print(search_in_matrix(matrix, target))

print('*******************************************************************************')

from itertools import product

def search_in_matrix2(matrix, target):
    matrix_length = len(matrix)

    gen = ( (i,j)   for i in range(matrix_length)   for j in range(len(matrix[i])) )
    for i,j in gen:

        element = matrix[i][j]

        if element == target: return f'The target is at position {[i,j]} in the matrix.'

    return [-1, -1]

print(search_in_matrix2(matrix, target))


print('*******************************************************************************')

if __name__ == '__main__':
    main()