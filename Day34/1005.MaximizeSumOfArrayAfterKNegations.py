from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0 
        while i < len(nums) and nums[i] < 0 and k > 0: 
            nums[i] = -nums[i]
            i += 1
            k -= 1

        if k % 2 != 0: 
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)