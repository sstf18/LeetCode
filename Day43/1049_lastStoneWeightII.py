from ast import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        dp = [0] * 3001
        total_sum = sum(stones)
        target = total_sum // 2

        for stone in stones:
            print("_____")
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
                print(dp[j])

        return total_sum - dp[target] - dp[target]