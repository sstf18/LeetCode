# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from ast import List
from collections import defaultdict
from typing import Optional


class Solution:

    def searchBST (self, cur ,freq_map):
        if cur is None: 
            return 
        freq_map[cur.val] += 1
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = defaultdict(int)
        result = []
        if root is None: 
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq: 
                result.append(key)
        return result 