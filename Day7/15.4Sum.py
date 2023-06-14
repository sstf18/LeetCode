from ast import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            # 剪枝 
            # this target could be negative, so nums[i] > target
            if nums[i] > target and nums[i] > 0 and target > 0: 
                break 
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # j is ahead of i 
            for j in range(i+1, n):
                # add i and j to do cut .. 
                if nums[i]+nums[j] > target and target > 0: 
                    break 
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j+1
                right = n-1
                while left < right: 
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s == target: 
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target: 
                        left += 1
                    else: 
                        right -= 1

        return result 

# !!!! harder than 454 "4Sum"
# since this one need the unique quadruplets [nums[a], nums[b], unms[c], nums[d]]
# and this one find the answer in one list, not in multiple list. 
# samiliar with 3Sum one, with one more for loop. 