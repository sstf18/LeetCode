from typing import List

# dp arrary: dp[i][j]
# formula: add a if statement, dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# dp init: dp[i][0] = 1, dp[0][j] = 1
# train sequence

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # obstackeGrid is 2d arrary
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # the point of start and end has obstacle
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1: 
            return 0 
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            # meet the grid
            if obstacleGrid[i][0] == 0: 
                dp[i][0] = 1
            else: 
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0 : 
                dp[0][j] = 1
            else: 
                break
        for i in range(1, m):
            for j in range(1, n):
                # if there's an obstacle at the current cell, the loop skips to the next iteration. 
                if obstacleGrid[i][j] == 1: 
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]