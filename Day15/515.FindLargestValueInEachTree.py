# Definition for a binary tree node.

import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        result = []

        if not root: 
            return []
        
        
        while queue: 
            max_val = float('-inf')
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.appendleft()
                max_val = max(max_val, cur.val)

                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
            result.append(max_val)
        return result

