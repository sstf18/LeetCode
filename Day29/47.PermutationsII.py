from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False]*len(nums)
        self.backTracking(nums, used, [], result)
        return result

    def backTracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return 

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1] and not used[i-1]:
                continue
            if used[i]: 
                continue

            used[i] = True
            path.append(nums[i]) 
            self.backTracking(nums, used, path, result)
            used[i] = False
            path.pop()
            

