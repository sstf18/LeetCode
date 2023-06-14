# input: s = 'abcdefg', k = 2
# output: 'cdefgab'

# using cut method

class Solution: 
    def leftTurnChar(self, s: str, k: int) -> str: 
        new_s  = s[k:]+ s[:k]
        return new_s

solution = Solution()
input1 = 'abcdef'
solution1 = solution.leftTurnChar(input1, 2)
print(solution1)

#Thinking: 
# learned how to create a instance 
# and create a test code