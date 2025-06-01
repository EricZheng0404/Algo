"""
LeetCode 270. Closest Binary Search Tree Value
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res = root.val
        self.delta = float('inf')
        self.traverse(root, target)
        return self.res
    
    def traverse(self, root, target):
        if root is None:
            return 
        newDelta = root.val - target
        if abs(newDelta) == self.delta and root.val < self.res:
            self.res = root.val
        if abs(newDelta) < abs(self.delta):
            self.delta = newDelta
            self.res = root.val
        if root.val == target:
            return
        elif root.val > target:
            self.traverse(root.left, target)
        else:
            self.traverse(root.right, target)