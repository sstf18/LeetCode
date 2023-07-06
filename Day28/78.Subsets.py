from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backTracking(nums, 0 , path, result)
        return result


    def backTracking(self, nums, startIndex, path, result):
        result.append(path[:])
        if startIndex >= len(nums):
            return 

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backTracking(nums, i+1, path, result)
            path.pop()

