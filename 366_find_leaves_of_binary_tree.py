# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.traversal(root)
        return self.res
    
    def traversal(self, root):
        if root is None:
            return 0
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        height = max(left, right) + 1
        # if this is a new height that's not added to the list
        if len(self.res) < height:
            self.res.append([])
        # We add the value to its height index
        self.res[height - 1].append(root.val)
        return height


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.findLeaves(root))