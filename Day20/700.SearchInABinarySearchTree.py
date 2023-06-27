# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # limit
        if not root or root.val == val:
            return root 

        result = TreeNode()
        # left
        if val < root.val: 
            result = self.searchBST(root.left, val)
        # right
        if val > root.val: 
            result = self.searchBST(root.right, val)
        return result 
        
        # this is the iterator way, mach simple than recursion 

        # while root: 
        #     if val < root.val: 
        #         root = root.left 
        #     elif val > root.val: 
        #         root = root.right 
        #     else: 
        #         return root 
        # return None