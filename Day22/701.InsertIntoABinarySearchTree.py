# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # create a new node
        if root is None: 
            node = TreeNode(val)
            return node
            
        if val < root.val: 
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val: 
            root.right = self.insertIntoBST(root.right, val)

        return root

