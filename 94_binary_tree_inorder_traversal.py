"""
LeetCode 94. Binary Tree Inorder Traversal
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return 
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
        