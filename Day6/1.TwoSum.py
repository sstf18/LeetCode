from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = set()
        for i, num in enumerate(nums):
            complement = target - num

            if complement in result:
               return [nums.index(complement), i]
            result.add(num)
    
# using set() method
# !!!!!!!!1

# in the first iteration: 'num' is 2. 'complement = 9-2=7', '7' is no in result
# the number '2' is added to the 'result' set using 'result.add(num)'

# second iteration: 'num' is 7. 'complement 9 -7 = 2' , '2' in the result
# The line return [nums.index(complement), i] is executed.
# nums.index(complement) returns the index of the complement 2 in the nums list, which is 0.
# 'i' is the index of the current number 7, which is 1.
# The code returns the list [0, 1]
