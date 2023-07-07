from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        count = 0 
        # in a for loop to train len(nums)
        for i in range(len(nums)):
            # count is the cursum, which always add the next value
            count += nums[i]
            # re-compare the count and result
            if count > result: 
                # re-asign the result
                result = count
            if count <= 0 : 
                count = 0 
        return result 

