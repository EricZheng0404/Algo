"""
LeetCode 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

"""

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # The final result
        self.res = True
        # Traverse the tree and check if it is balanced
        self.traverse(root)
        return self.res

    def traverse(self, root):

        # if self.res is False:
        #     return
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # Post-order position: when we already know the height of the left and 
        # right subtrees, we can check if the tree is balanced
        if abs(left - right) > 1:
            self.res = False
        return 1 + max(left, right)