from typing import Optional
"""
114. Flatten Binary Tree to Linked List
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        # We flatten left and right branches
        self.flatten(root.left)
        self.flatten(root.right)
        # Post-order position
        # Up to this point, both left and right branches are sorted already
        left, right = root.left, root.right
        # Set the left child pointer to None
        root.left = None
        root.right = left
        p = root
        # We need to the last node that's not a None
        while p.right:
            # In the last iteration, p is pushed to the right end of the branch
            p = p.right
        p.right = right

    
        