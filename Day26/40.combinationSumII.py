from ast import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backTracking(candidates, target, 0 , 0, [], result)
        return result

    def backTracking(self, candidates, target, curSum,startIndex, path, result):
        if curSum > target: 
            return 
        if curSum == target: 
            result.append(path[:])
            return 
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i -1]:
                continue
            if curSum + candidates[i] > target: 
                break

            path.append(candidates[i])
            curSum += candidates[i]
            self.backTracking(candidates, target, curSum, i+1, path, result)
            curSum -= candidates[i]
            path.pop()