# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # ietrator: pre-ordered  

        # queue = collections.deque([root])
        # if not root: 
        #     return None

        # while queue: 

        #     cur = queue.popleft()
        #     cur.left, cur.right = cur.right, cur.left
        #     if cur.left: 
        #         queue.append(cur.left)
        #     if cur.right: 
        #         queue.append(cur.right)
    
        # return root

        if not root: 
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root