#Time: O(mn)
#Space: O(mn)
#Dynamic Programming
#https://leetcode.com/problems/unique-paths/
def uniquePaths( m: int, n: int) -> int:
        matrix = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return matrix[m-1][n-1]

print(uniquePaths(3,7))
