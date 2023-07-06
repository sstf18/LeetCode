from ast import List

class Solution:
    def partition(self, s: str) -> List[List[str]]: 
        result = []
        self.backTracking(s, 0, [], result)
        return result

    def backTracking(self, s, startIndex, path, result) :
        # base case
        if startIndex >= len(s):
            result.append(path[:])
            return 

        # single level traversal
        for i in range(startIndex, len(s)):
            # if it is palmdrone
            if self.isPalindrome(s, startIndex, i):
                path.append(s[startIndex: i+1])
                self.backTracking(s, i + 1, path, result)
                path.pop()

    def isPalindrome(self, s:str, start: int, end: int):

        while start < end: 
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

