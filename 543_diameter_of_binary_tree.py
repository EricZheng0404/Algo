"""
Leetcode 543: Diameter of Binary Tree
This is a binary tree problem.
The goal is to find the diameter of the binary tree.
The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.dia

    def maxDepth(self, root):
        if not root:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        length = leftMax + rightMax
        self.dia = max(self.dia, length)
        return 1 + max(leftMax, rightMax)