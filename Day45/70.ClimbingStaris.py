class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0: 
        #     return 0
        # dp = [0] * (n + 2)
        # dp[1] = 1 
        # dp[2] = 2

        # for i in range(3, n+2):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        dp = [0] * (n + 1)
        dp[0] = 1 
        m = 2
        # train the backpack
        for j in range( n + 1):
            # step = 1 or 2
            for step in range(1, m+1):
                # if step smaller than bagSize
                if step <= j: 
                    dp[j] += dp[j - step]

        return dp[n]
