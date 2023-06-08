#Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place. 

#example: Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]

from ast import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 
        fast = 0 
        size = len(nums)
        while fast < size: 
            if nums[fast] != val: 
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 
        return slow 


#thinking: using two pointer, slow and fast
#when target == fast, fast move 1 step, slow doesnt move 
#when target != fast, fast and slow both move 1 step 