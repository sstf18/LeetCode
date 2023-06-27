#给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
# 这条路径上所有节点值相加等于目标和。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        return self.traversal(root, targetSum - root.val)


    
    def traversal(self, cur: TreeNode, count: int): 
        if not cur.left and not cur.right and count == 0: 
            return True 
        if not cur.left and not cur.right and count != 0: 
            return False
        if cur.left: 
            count -= cur.left.val
            if self.traversal(cur.left, count):
                return True
            count += cur.left.val

        if cur.right: 
            count -= cur.right.val
            if self.traversal(cur.right, count):
                return True
            count += cur.right.val
        return False