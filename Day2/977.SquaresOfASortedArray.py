from ast import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) - 1
        i= len(nums) - 1
        res = [float('inf')] * len(nums)

        while left <= right: 
            if nums[left] ** 2 < nums[right] ** 2: 
                res[i] = nums[right]** 2 
                right -= 1
            else: 
                res[i] = nums[left]**2
                left += 1
            i -= 1

        return res

#thinking: 
#1. be care for the init for 'res', [float('inf')] means that
#  the in infinit number times len(nums) provid the answer cross the line
#2. for the right hand side, since the left is 0, the right must be len(nums) -1 
#3. remaber to move the index of res. 