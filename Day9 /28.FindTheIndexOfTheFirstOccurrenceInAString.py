from typing import List


class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try: 
    #         return haystack.index(needle)
    #     except ValueError:
    #         return -1
    def getNext(self, next: List[int], s: str) -> None:
        #init 
        j = 0
        next[0] = 0
        # if front and back is not equal 
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            # if front and back is equal
            if s[i] == s[j]:
                j += 1
            # update
            next[i] = j
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        # init 
        j = 0
        # if not equal 
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            # if equal 
            if haystack[i] == needle[j]:
                j += 1
            # update
            if j == len(needle):
                # since i start from 0, and len(needle) start from 1
                # so it should add 1 in the later
                return i - len(needle) + 1
        return -1

    # init 
    # front and back is not equal 
    # front and back is equal 
    # update 