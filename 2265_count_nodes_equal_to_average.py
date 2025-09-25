# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        self.subProblem(root)
        return self.res
    
    def subProblem(self, root):
        if root is None:
            # The total number of nodes, and the sum of all the nodes
            return [0, 0]
        left = self.subProblem(root.left)
        right = self.subProblem(root.right)
        numNodes = 1 + left[0] + right[0]
        totalValue = root.val + left[1] + right[1]
        if totalValue // numNodes == root.val:
            self.res += 1
        return [numNodes, totalValue]
