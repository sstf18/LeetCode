from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        self.backTracking(nums, 0 , used, path, result)
        return result


    def backTracking(self, nums, startIndex, used, path, result):
        result.append(path[:])

        for i in range(startIndex, len(nums)):
            # 
            if i > 0 and nums[i] == nums[i -1] and not used[i-1]:
                continue
            path.append(nums[i])
            used[i] =True
            self.backTracking(nums, i+1, used, path, result)
            used[i] =False
            path.pop()