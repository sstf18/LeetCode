

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        # nxt[-1] the last element of the 'nxt' array
        # for example: [0,0,1,2,3,4]
        # nxt[-1] = 4
        # len(s) = 6, len(s) - nxt[-1] = 6-4 =2
        # len(s) modulo 2 is 0
        if nxt[-1] != 0 and len(s) % (len(s) - (nxt[-1])) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt