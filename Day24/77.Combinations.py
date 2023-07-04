from ast import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backTracking(n, k, 1, [], result)
        return result

    def backTracking(self, n, k, startIndex, path, result):
        if len(path) == k: 
            result.append(path[:])
            return
        for i in range (startIndex, n + 1):
            path.append(i)
            self.backTracking(n, k, i +1, path, result)
            path.pop()

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []
#         self.backTracking(n, k, 1, [], result)
#         return result


#     def backTracking(self, n, k, startIndex, path, result):
#         if len(path) == k: 
#             result.append(path[:])
#             return
#         for i in range (startIndex, n -(k - len(path)) + 2):
#             path.append(i)
#             self.backTracking(n, k, i +1, path, result)
#             path.pop()

# in this code, it decrease the size of the for loop