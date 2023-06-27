# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(0)

        maxVal = 0 
        maxVal_idx = 0
        # middle
        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxVal_idx = i 
        node.val = maxVal

        # left
        if maxVal_idx > 0:
            new_list = nums[:maxVal_idx]
            node.left = self.constructMaximumBinaryTree(new_list)

        # right
        if maxVal_idx < len(nums) -1: 
            new_list = nums[maxVal_idx + 1:]
            node.right = self.constructMaximumBinaryTree(new_list)
        return node