# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)

    def traversal(self, node):
        if not node: 
            return (0, 0)

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # do not rob curr, cur child 
        val_0 = max(left[0], left[1]) + max(right[0], right[1])
        # 
        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)