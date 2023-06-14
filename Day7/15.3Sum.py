from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            #剪枝
            if nums[i] > 0: 
                return result
            #去重
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            left = i+1 
            right = len(nums) - 1

            while left < right: 
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ > 0: 
                    right -= 1
                elif sum_ < 0: 
                    left += 1
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                    #去重
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
        return result
# be careful the second part(left and right )
        