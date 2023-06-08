# Given an array of integers nums which is sorted in ascending order, 
# an integer target, write a function to search traget in nums. If target exists,
# then return its index. Otherwise return -1. 

#example: Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4

from ast import List

class Solution:
    #left close, right open
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)
        while left < right: 
            middle = (right + left) // 2 # this way is used to avoid potential integer overflow
            #left+(right - left)//2
            if nums[middle] > target: 
                right = middle
            elif nums[middle] < target: 
                left = middle + 1
            else: 
                return middle 
        return -1

    #left close, right close
    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0 
    #     right = len(nums)-1
    #     while left <= right: 
    #         middle = (right + left) // 2 
    #         if nums[middle] > target: 
    #             right = middle - 1
    #         elif nums[middle] < target: 
    #             left = middle + 1
    #         else: 
    #             return middle 
    #     return -1

#Thinking: 
#most important thing is that remeber 
# "left close, right close" or "left close, right open"
# als0, for middle function: left+(right - left)//2