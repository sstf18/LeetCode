# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # queue = collections.deque([root])
        # count = 0

        # if not root: 
        #     return 0 
        # while queue: 
        #     level_size = len(queue)
        #     for _ in range(level_size):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right: 
        #             queue.append(cur.right)
        #         count += 1
        # return count


        if not root: 
            return 0 
        left = root.left
        right = root.right
        leftDepth = 0 
        rightDepth = 0 
        while left: 
            left = left.left
            leftDepth += 1
        while right: 
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth: 
            return (2 << leftDepth) -1 
        return self.countNodes(root.left) + self.countNodes(root.right) + 1