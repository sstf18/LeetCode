class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0 
        dp[1] = 0  
        dp[2] = 1

        for i in range(3, n + 1):
            # i//2 + 1: by the math, if the number close to each other, the produce of numbers are biggest. 
            for j in range(1, i // 2 + 1):
                # j * (i - j): break into two numbers
                # j * dp[i -j]: dp[i - j] is the break rest of (i-j)
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        return dp[n]
