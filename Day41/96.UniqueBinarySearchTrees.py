class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            print("........")
            # j is the current head node. 
            for j in range(1, i + 1):
                # dp [j - 1]: left tree
                # dp [i - j]: right tree
                dp[i] += dp[j - 1] * dp[i - j]
                print(dp[i])
        return dp[n]