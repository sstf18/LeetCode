from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False]*len(nums)
        self.backTracking(nums, used, [], result)
        return result

    def backTracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return 

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backTracking(nums, used, path, result)
            used[i] = False
            path.pop()
