from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # if day[i-1]>day[i], skip to day[i]
        result = 0 
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result 