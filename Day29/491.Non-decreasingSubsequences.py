from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        self.backTracking(nums, 0, [], result)
        return result

    def backTracking(self, nums, startIndex, path, result):
        if len(path) > 1: 
            result.append(path[:])
        uset = set()
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:
                continue
                
            uset.add(nums[i])
            path.append(nums[i])
            self.backTracking(nums, i+1, path, result)
            path.pop()