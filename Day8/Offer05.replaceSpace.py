# input: "We are happy."
# Output: "We%20are%20happy."

class Solution:
    def replaceSpace(self, s: str) -> str : 
        res = []
        for i in range(len(s)):
            if s[i] == ' ':
                res.append('%20')
            else:
                res.append(s[i])
        return ''.join(res)

# since s is a string, and res is a list
# so we using list, store the res in it, 
# then using .join(res) concentrate them together
# and `''` is an separator
