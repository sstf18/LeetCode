class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for i in range(len(s)):
            if res and s[i] == res[-1]:
                res.pop()
            else: 
                res.append(s[i])
        return "".join(res) 

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         for i in range(len(s)):
#             if stack and s[i] == stack[-1]:
#                 stack.pop()
#             else: 
#                 stack.append(s[i])
#         return "".join(stack) 

# Thinking: 
# using the list() as the data strucutres of the stack
# is res is not empty and s[i] == res[-1](last element)

