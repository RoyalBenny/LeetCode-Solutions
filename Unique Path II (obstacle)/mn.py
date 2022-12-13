#Time : O(mn)
#Space: O(nm)
#Dynamic Programming
# https://leetcode.com/problems/unique-paths-ii/
def uniquePathsWithObstacles(obstacleGrid) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        output = [[0]*(n) for _ in range((m))]
        output[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(1,n):
            if obstacleGrid[0][i] !=1:
                output[0][i] = output[0][i-1]
        for i in range(1,m):
            if obstacleGrid[i][0] !=1:
                output[i][0] = output[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    output[i][j] = output[i-1][j]+output[i][j-1]
        return output[m-1][n-1]
print(uniquePathsWithObstacles([[0,0,0],[1,1,0],[0,0,0]]))
