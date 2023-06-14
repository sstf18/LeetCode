from ast import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        for n1 in nums1: 
            for n2 in nums2:
                if n1+n2 in hashmap: 
                    hashmap[n1 + n2] += 1
                else: 
                    hashmap[n1 + n2] = 1
        
        count = 0
        for n3 in nums3: 
            for n4 in nums4: 
                if -(n3 + n4) in hashmap:
                    count += hashmap[n3+n4]
        return count

# since this question ask 4 sum in 4 integer arrays
# and the output could be the same with previously
# !!!!! hashmap[n1+n2] = 1 not hashmap[n1+n2] == 1
# reason: the code is not checking for equality ('==') with 1
# becasue the puarpose is to count the frequencies of the sums, not to check 
# if the sum is exactly equal to 1