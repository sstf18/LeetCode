from ast import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backTracking(candidates, target, 0 , 0, [], result)
        return result

    def backTracking(self, candidates, target, curSum,startIndex, path, result):
        if curSum > target: 
            return 
        if curSum == target: 
            result.append(path[:])
            return 
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            curSum += candidates[i]
            self.backTracking(candidates, target, curSum, i, path, result)
            curSum -= candidates[i]
            path.pop()