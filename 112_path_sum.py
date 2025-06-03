"""
Given a binary tree and a target sum, return true if there is a root-to-leaf path
such that adding up all the values along the path equals the target sum.

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree: (1 --> 2): The sum is 3. (1 --> 3): The sum is 4. There is no root-to-leaf path with sum = 5.
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

"""
The idea is that traversal function only helps when we walk through all the path,
but we need to set other variables we want aside as instance variables.
"""
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        self.sum_ = 0
        self.traverse(root, targetSum)
        return self.found 

    def traverse(self, root, targetSum):
        if root is None:
            return
        self.sum_ = self.sum_ + root.val
        if root.left is None and root.right is None:
            if self.sum_ == targetSum:
                self.found = True
        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)
        self.sum_ -= root.val