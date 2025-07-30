"""
Leetcode 98: Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    The root must greater than all the nodes in the left subtree and less 
    than all the nodes in the right subtree.

    
   
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
    
    def validate(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high: 
            return False
        return self.validate(root.left, low, root.val) and self.validate(root.right, root.val, high)