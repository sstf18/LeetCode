# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1: 
            return True
        else: 
            return False

    def getHeight(self, root: TreeNode) -> int: 
        if not root: 
            return 0
       
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
         #left
        if leftHeight == -1:
            return -1 
        #right
        if rightHeight == -1: 
            return -1 
        # middle 
        if abs(leftHeight - rightHeight) > 1: 
            return -1 
        else: 
            return 1 + max(leftHeight, rightHeight)

#Thinking: 
# this quesion need  more time to review
# need to understand why there are a lots of '-1'
        