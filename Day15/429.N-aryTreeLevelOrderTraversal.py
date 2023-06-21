
# Definition for a Node.
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: 
            return []

        queue = collections.deque([root])
        result = []

        while queue: 
            level = []
            queue_size = len(queue)
            for _ in range(queue_size):
                cur = queue.popleft()
                level.append(cur.val)
                for child in cur.children: 
                    queue.append(child)

            result.append(level)
        return result
