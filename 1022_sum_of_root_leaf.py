"""
LeetCode 1022. Sum of Root To Leaf Binary Numbers

Input:
- A binary tree

Output:
- The sum of all root-to-leaf binary numbers
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        self.res = 0
        self.traverse(root)
        return self.res

    def traverse(self, root: TreeNode):
        if root is None:
            return
        if root.left is None and root.right is None:
            # leaf node
            self.res += self.path << 1 | root.val
            return
        # pre-order position
        self.path = self.path << 1 | root.val
        self.traverse(root.left)
        self.traverse(root.right)
        # post-order position
        self.path = self.path >> 1