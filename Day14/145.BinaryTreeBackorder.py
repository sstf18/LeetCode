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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #recursion: 

        # if not root: 
        #     return []
        
        # left = self.postorderTraversal(root.left)
        # right = self.postorderTraversal(root.right)

        # return left + right + [root.val]


        # iteritor: 
        
         # if no root node, return nothing
        if not root: 
            return []

        # add root node into stack
        stack = [root]
        result = []

        # if stack is not empty 
        while stack: 
            # first pop the first node
            node = stack.pop()
            # then add it into result
            result.append(node.val)
            # if there is left add to left
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        
        return result[::-1]
