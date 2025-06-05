"""
LeetCode 101. Symmetric Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val 
                and self.check(left.right, right.left)
                and self.check(left.left, right.right))