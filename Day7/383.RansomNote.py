class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result= [0]*26
        for i in magazine: 
            result[ord(i)-ord('a')] += 1
        for i in ransomNote: 
            result[ord(i)-ord('a')] -= 1
        for i in range(26):
            if result[i] < 0: 
                return False
        return True

# Thining: ord() founciton is used to get the Unicode code point of a character. 