from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0 
        dp = [0] * 10001
        for num in nums: 
            _sum += num

        if _sum % 2 == 1: 
            return False 
        target = _sum // 2 

        # set num is 'i' and nums is 'weight'
        for num in nums: 
            # target is weightBag
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)

        if dp[target] == target: 
            return True 

        return False 