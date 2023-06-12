# method 1: Array
from ast import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #we use array because of nums.length <= 1000
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for i in range(len(nums2)):
            count2[nums2[i]] += 1
        for k in range(1001):
            if count1[k]*count2[k] > 0:
                result.append(k)
        
        return result

# method 2: set 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# set() founction is a way to get the intersection
