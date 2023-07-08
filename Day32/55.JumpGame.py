from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0 
        if len(nums) == 1: 
            return True 
        for i in range(len(nums)):
            if i <= cover: 
                cover = max(i + nums[i], cover)
                # 0,1,2,3,4 => len(nums)-1 = 4
                if cover >= len(nums) - 1:
                    return True
        return False