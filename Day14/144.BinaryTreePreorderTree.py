# Definition for a binary tree node.
from ast import List
from typing import Optional

# Using recursion 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursion: 

        # if not root: 
        #     return []

        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)

        # return [root.val] + left + right

        if not root: 
            return []
        stack = [root]
        result = []
        while stack: 
            node = stack.pop()
            result.append(node.val)
            if node.right: 
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
        return result

