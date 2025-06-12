"""
LeetCode 226. Invert Binary Tree
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
    
    def traverse(self, root):
        # Base case: if the root is None, we return.
        if root is None:
            return 
        # Swap the left and right children.
        temp = root.right
        root.right = root.left
        root.left = temp
        self.traverse(root.left)
        self.traverse(root.right)

class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
    
    def traverse(self, root):
        if root is None:
            return