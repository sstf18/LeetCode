from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 

        # train items
        for coin in coins: 
            #train backsize
            for i in range(coin, amount + 1): 
                if dp[i - coin] != float('inf'): 
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[amount] == float('inf'):
            return - 1

        return dp[amount]