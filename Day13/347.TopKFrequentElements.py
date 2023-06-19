from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums: 
            if num in freq_map: 
                freq_map[num] += 1
            else: 
                freq_map[num] = 1
        
        sorted_freq = sorted(freq_map.items(), key=lambda x:x[1], reverse = True)
        top_k_freq = []
        for num, count in sorted_freq[:k]:
            top_k_freq.append(num)
        return top_k_freq

# Thinking: 
# using map to find the frequency of each elements 
# += 1 for specific elements, 
# then sort the elements in map from most to less 
# find the 'K' the elements