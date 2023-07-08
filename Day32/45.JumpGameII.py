from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cur_distance = 0
        ans = 0 
        next_distance = 0 

        for i in range(len(nums)):
            next_distance = max(nums[i]+i, next_distance)
            if i == cur_distance: 
                ans += 1
                cur_distance = next_distance
                if next_distance >= len(nums) -1: 
                    break
             
        return ans