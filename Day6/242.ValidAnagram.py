class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        records = [0]*26
        for i in s: 
            records[ord(i) - ord("a")] += 1
        for i in t: 
            records[ord(i) - ord("a")] -= 1
        for k in range(26):
            if records[k] != 0:
                return False
        return True