from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort the g and s 
        #child
        g.sort()
        #cookies
        s.sort()
        index = len(s)-1
        result = 0 

        for i in range(len(g)-1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1
        return result

