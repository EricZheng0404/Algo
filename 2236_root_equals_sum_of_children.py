"""
Given a binary tree, return true if the root equals the sum of the values of all its descendants.

Example:

Input: root = [10, 4, 6]
Output: true

Input: root = [5, 3, 1]
Output: false

Input: root = [10, 4, 6]
Output: true
"""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    We still need to traverse the tree to get the sum of the descendants.
    We can use a helper function to do this.
    """
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.sumDescendants(root.left)
        right = self.sumDescendants(root.right)
        return root.val == left + right

    def sumDescendants(self, root):
        if not root:
            return 0
        return root.val + self.sumDescendants(root.left) + self.sumDescendants(root.right)