"""
Leetcode 543: Diameter of Binary Tree
This is a binary tree problem.
The goal is to find the diameter of the binary tree.
The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.dia

    def maxDepth(self, root):
        if not root:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        length = leftMax + rightMax
        self.dia = max(self.dia, length)
        # leftMax and rightMax are the diameter for these two subtrees.
        # But to get to the root and get the biggest diameter for the 
        # root, we need to the max between them + 1.
        return 1 + max(leftMax, rightMax) # This is the max depth of the current node.
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))