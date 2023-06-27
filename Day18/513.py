# given a binary tree, find the most left element in the last level 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        self.max_depth = float('-inf')
        self.result = None
        self.traveral(root, 0)
        return self.result

    def traversal(self, node, depth):
        if not node.left and not node.right: 
            if depth > self.max_depth: 
                self.max_depth = depth
                self.result = node.val
            return 
    
        if node.left: 
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right: 
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1