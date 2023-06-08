from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0 
        res = float('inf')
        curr_sum = 0 
        #using for loop and while loop are same
        #but, need take care of i. and i didnot use i actually. 
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[right]
            while curr_sum >= target: 
                res = min(res, right - left + 1)
                curr_sum = curr_sum - nums[left]
                left += 1
            right += 1
                
        if res != float('inf'):
            return res
        else: 
            return 0 

    # Thinking: 
    # this question still use two pointers, but need way to use it
    # which is salding window!! 