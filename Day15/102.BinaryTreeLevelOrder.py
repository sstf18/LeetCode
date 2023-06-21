

from ast import List
import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # set a array to store the 
    #     levels = []
    #     self.helper(root, 0, levels)
    #     return levels

    # def helper(self, node, level, levels):
    #     if not node: 
    #         return 
    #     if len(levels) == level: 
    #         levels.append([])
    #     levels[level].append(node.val)
    #     self.helper(node.left, level + 1, levels)
    #     self.helper(node.right, level + 1, levels)


        if not root: 
            return []

        queue = collections.deque([root])
        result = []

        while queue: 
            # contains the values of all the nodes in that level
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
            result.append(level)
        return result 