# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ensure result is an empty list
        self.result = []

        self.traversal(root)

        for i in range(1, len(self.result)):
            if self.result[i] <= self.result[i - 1]:
                return False
        return True
        #inorder traversal is increasing!!!!!


    def traversal(self, cur):
        if not cur: 
            return True 
        self.traversal(cur.left) 
        self.result.append(cur.val)
        self.traversal(cur.right)