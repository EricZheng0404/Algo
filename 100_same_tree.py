"""
LeetCode 100. Same Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p, q)
    
    def traverse(self, p, q):
        # Base case: if both are None, return True
        if p is None and q is None:
            return True
        # If one is None and the other is not, return False
        if p is None or q is None:
            return False
        # If the values are different, return False
        if p.val != q.val:
            return False
        left = self.traverse(p.left, q.left)
        right = self.traverse(p.right, q.right)
        return left and right