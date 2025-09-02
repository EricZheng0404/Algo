from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = float("-inf")
        self.sub(root)
        return self.res
    
    def sub(self, root):
        if not root:
            return 0
        leftSum = max(0, self.sub(root.left))
        rightSum = max(0, self.sub(root.right))
        # This curr means if the current root is the final answer
        # That means we go through it from left to right tree
        curr = root.val + leftSum + rightSum
        self.res = max(self.res, curr) 
        # If the current root is not the answer, then we can pick only
        # either the left or the right tree
        return max(leftSum, rightSum) + root.val