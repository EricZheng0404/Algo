"""
Leetcode 144: Binary Tree Preorder Traversal
This is a binary tree problem.
The goal is to traverse the binary tree in preorder.
Preorder traversal is to visit the root node first, then the left subtree, 
then the right subtree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution 1: Recursive traversal
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

"""
Solution 2: Subproblem
"""
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res