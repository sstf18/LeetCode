# Definition for a binary tree node.

import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = collections.deque([root])
        result = []

        if not root: 
            return []
        while queue: 
            queue_size = len(queue)
            for i in range(queue_size):
                cur = queue.popleft()
                if i == queue_size - 1:
                    result.append(cur.val)
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
        return result