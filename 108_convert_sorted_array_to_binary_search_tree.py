"""
LeetCode 108. Convert Sorted Array to Binary Search Tree
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums, 0, len(nums) - 1)

    def makeTree(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.makeTree(nums, left, mid - 1)
        root.right = self.makeTree(nums, mid + 1, right)
        return root