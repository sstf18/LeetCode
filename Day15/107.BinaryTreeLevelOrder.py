# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from ast import List
import collections
from typing import Optional


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        result = []

        if not root: 
            return []
        while queue: 
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
            result.append(level)
        return result[::-1]