class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def reverse_substring(text):
            left = 0
            right = len(text) - 1
            while left < right: 
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)
        for i in range(0, len(s), 2*k):
            res[i: i + k] = reverse_substring(res[i: i + k])
        return ''.join(res)
#  create a reverse function, same with last question 
# using for loop, and loop 2*k in every iteration 