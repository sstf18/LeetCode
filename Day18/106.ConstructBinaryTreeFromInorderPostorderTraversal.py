# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # tree is Null
        if not postorder: 
            return None

        # the last element is root 
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # the index of separator
        separator_idx = inorder.index(root_val)

        # using separator to cut inorder
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        #using separator to cut postorder
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # recursion
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root