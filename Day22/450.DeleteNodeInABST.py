# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #1. can not find the 'key' in treeNode
        #2. 'key' is leaf node
        #3. 'key' left is not None, right is None
        #4. 'key' left is None, right is not None
        #5. 'key' left and right both is not None
        if root is None: 
            return None 
        if root.val == key: 
            if root.left is None and root.right is None: 
                return None
            elif root.left is not None and root.right is None: 
                return root.left
            elif root.left is None and root.right is not None: 
                return root.right
            elif root.left is not None and root.right is not None: 
                cur = root.right
                while cur.left: 
                    cur = cur.left
                cur.left = root.left
                return root.right
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        return root

