# Definition for a binary tree node.
from ast import List
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: 
            return []

        queue = collections.deque([root])
        avg_queue = []

        while queue: 

            queue_size = len(queue)
            level_sum = 0
            for i in range(queue_size):
                cur = queue.popleft()

                level_sum += cur.val

                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
            avg_queue.append(level_sum / queue_size)
        return avg_queue