from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            print("--------")
            for j in range(coins[i], amount + 1):
                print(j)
                print("++++++")
                #print(coins[i])
                dp[j] += dp[j - coins[i]]
        return dp[amount]