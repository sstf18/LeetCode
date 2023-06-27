# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: 
            return root2
        if not root2: 
            return root1

        root = TreeNode()
        # middle
        root.val = root1.val + root2.val
        # left
        root.left = self.mergeTrees(root1.left, root2.left)
        # right
        root.right = self.mergeTrees(root1.right, root2.right)
        return root