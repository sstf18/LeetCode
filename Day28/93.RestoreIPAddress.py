from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backTracking(s, 0, 0, "", result)
        return result 

    def backTracking(self, s, startIndex, pointSum, current, result):
        if pointSum == 3: 
            # if the fourth result is valid
            if self.isValid(s, startIndex, len(s) - 1):
                current += s[startIndex:]
                result.append(current)
            return
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                sub = s[startIndex:i + 1]
                self.backTracking(s, i + 1, pointSum + 1,current + sub + '.', result)
            else: 
                break

    def isValid(self, s, start, end):
        if start > end: 
            return False
        if s[start] == '0' and start != end: 
            return False
        num = 0 
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False 
        return True

