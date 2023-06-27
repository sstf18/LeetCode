# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        # result: store the final result
        self.result = []

        # temporarily hold the current path being traversed
        self.path = []


    def traversal(self, cur, count):
        # valid path is found
        if not cur.left and not cur.right and count == 0: 
            self.result.append(self.path[:])
            return 

        # does not sum up to the target sum
        if not cur.left and not cur.right:
            return 

        if cur.left: 
            self.path.append(cur.left.val)
            count -= cur.left.val
            self.traversal(cur.left, count)
            # backtrack
            count += cur.left.val
            self.path.pop()
        if cur.right: 
            self.path.append(cur.right.val)
            count -= cur.right.val
            self.traversal(cur.right, count)
            count += cur.right.val
            self.path.pop()
        return 

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        if not root: 
            return self.result 
        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)
        return self.result