'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

# Test case
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
target = 13

def searchMatrix(matrix, target):
    # Iterate through each row
    for x in matrix:
        # If the returned index is not -1, then the target exists in the matrix
        # Use a trycatch statement that way if the index function has an error, it means that the value is not in the matrix
        try:
            if x.index(target) >= 0:
                return True
        except:
            return False

print(searchMatrix(matrix, target))

