from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1: 
            return nums[0]

        result1 = self.robRange(nums, 0, len(nums) - 2)
        result2 = self.robRange(nums, 1, len(nums) - 1)
        return max(result1, result2)

    def robRange(self, nums: List[int], start: int, end: int):
        if end == start: 
            return nums[start]

        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            # save the current biggest in temp
            temp = curr_max
            # update
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp

        return curr_max