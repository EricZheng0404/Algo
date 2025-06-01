"""
LeetCode 257. Binary Tree Paths
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.path = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        self.path.append(str(root.val))
        if root.left is None and root.right is None:
            self.res.append("->".join(self.path))
        self.traverse(root.left)
        self.traverse(root.right)
        self.path.pop()