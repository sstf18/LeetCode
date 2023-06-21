# Definition for a binary tree node.

import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        depth = 0 

        if not root: 
            return 0 
        while queue: 
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
        return depth
        
