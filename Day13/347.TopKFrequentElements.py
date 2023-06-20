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

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # initalize dictinary, store the freq count of each integer in 'nums'
#         map_ = {}
#         for i in range(len(nums)):
#             map_[nums[i]] = map_get(nums[i], 0) + 1

#         # create an empty propority queue
#         pri_que = [] 

#         # key = i, freq = frequency count
#         for key, freq in map_.items():
#             #push a tuple(freq, key) onto the 'pri_que'
#             heapq.heappush(pri_que, (freq, key))
#             if len(pri_que) > k: 
#                 # remove the samllest element from the 'pri_que'
#                 heapq.headpop(pri_que)
#         result = [0]*k
#         for i in range(k-1, -1, -1):
#             result[i] = heapq.heappop(pri_que)[1]

#         return result

# Thinking: 
# using map to find the frequency of each elements 
# += 1 for specific elements, 
# then sort the elements in map from most to less 
# find the 'K' the elements