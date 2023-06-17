class Solution: 
    def validParentheses(self, s: str) -> bool: 
        stack = []
        for item in s: 
            if item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif item == '(':
                stack.append(')')
            # have to add 'not stack' at this step
            # stack[-1] means that 
            # in stack: )]}
            # stack[-1] = )
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        if not stack: 
            return True
        else: 
            return False 