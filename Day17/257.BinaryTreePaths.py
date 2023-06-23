# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: 
            return []
        result =[]
        path = []
        self.helper(root, path, result)
        return result

        
    def helper(self, cur, path, result):

        #middle
        path.append(cur.val)

        #move to leaf
        if not cur.left and not cur.right:
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        #left
        if cur.left: 
            self.helper(cur.left, path, result)
            path.pop()
        #right
        if cur.right: 
            self.helper(cur.right, path, result)
            path.pop()



