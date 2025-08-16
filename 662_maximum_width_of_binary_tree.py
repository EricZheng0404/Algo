from typing import Optional
"""
662. Maximum Width of Binary Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # To record the id of the leftmost node
        self.leftMost = []
        self.maxWidth = 0
        # We start with root, whose id is 1, depth is 1
        self.traverse(root, 1, 1)
        return self.maxWidth
    
    def traverse(self, root, id, depth):
        # Base case
        if not root:
            return
        # If it's the most left node: Whenever we get into a depth, 
        # there's one number lacking in the list, we upda the self.leftMost list
        if len(self.leftMost) == depth - 1:
            self.leftMost.append(id)
        # We try to update maxWidth every time by comparing the id of the node and the leftmost node 
        # in its depth
        self.maxWidth = max(self.maxWidth, id - self.leftMost[depth - 1] + 1)
        # The id of the left child is id * 2
        self.traverse(root.left, id * 2, depth + 1)
        # The id of the right child is id * 2 + 1
        self.traverse(root.right, id * 2 + 1, depth + 1)
