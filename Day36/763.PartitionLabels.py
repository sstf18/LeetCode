from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0]* 27 
        result = []
        # create a hash table, for each element
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i

        left = 0
        right = 0 
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right: 
                result.append(right - left + 1)
                left = i + 1

        return result  

        
