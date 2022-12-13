#Time : O(N^2)
#Space: O(1)
#String and array
# https://leetcode.com/problems/rotate-image/
def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix)!= len(matrix[0]):
            return 
        n = len(matrix)
        for first in range(n//2):
            last = n- first -1
            for i in range(first,last):
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = top
def printMatrix(matrix):
    for i in matrix:
        print(i)
    print()


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
printMatrix(matrix)
rotate(matrix)
printMatrix(matrix)


