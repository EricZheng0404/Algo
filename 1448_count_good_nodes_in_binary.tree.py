# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.traverse(root, root.val)
        return self.count
    
    def traverse(self, root, maxVal):
        if root is None:
            return
        if root.val >= maxVal:
            self.count += 1
        localMax = max(maxVal, root.val)
        self.traverse(root.left, localMax)
        self.traverse(root.right, localMax)
        