# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode((nums[0]))
        index = nums.index(max(nums))
        root = TreeNode(nums[index])
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:len(nums)])
        return root