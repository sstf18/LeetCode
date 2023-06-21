
# Definition for a Node.
import collections
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = collections.deque([root])
        if not root: 
            return root
        
        while queue: 
            level_size = len(queue)
            prev = None

            for i in range(level_size):
                cur = queue.popleft()
                if prev: 
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root