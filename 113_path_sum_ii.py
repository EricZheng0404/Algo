# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.path = []
        self.pathSum = 0
        self.traverse(root, targetSum)
        return self.res
    
    def traverse(self, root, targetSum):
        if root is None:
            return
        self.path.append(root.val)
        self.pathSum += root.val 
        if self.pathSum == targetSum and root.left is None and root.right is None:
            self.res.append(self.path[:])
        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)
        self.path.pop()
        self.pathSum -= root.val