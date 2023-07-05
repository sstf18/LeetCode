from ast import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backTracking(n, k, 0, 1, [], result)
        return result 

    # targetSum: the target sum
    def backTracking(self, targetSum, k, curSum, startIndex ,path,result):
        if curSum > targetSum: 
            return
        if len(path) == k: 
            if targetSum == curSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9- (k - len(path) + 2)):
            curSum += i 
            path.append(i)
            self.backTracking(targetSum, k, curSum, i + 1, path, result)
            curSum -= i
            path.pop()