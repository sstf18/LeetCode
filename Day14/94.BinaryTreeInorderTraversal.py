# Definition for a binary tree node.

from typing import List, Optional

# Using recursion 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursion: 

        # if not root: 
        #     return []
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)

        # return left + [root.val] + right

        # iterator: 
        if not root: 
            return []

        stack = []
        result = []
        cur = root
        while cur or stack: 
            if cur: 
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

# Thinking: 
# 1. if root is empty return []
# 2. inorder means left + root.val + right 
