from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: DFS
class Solution:
    def __init__(self):
        # record the minimum depth (the distance from the root to the nearest leaf node)
        self.minDepthValue = float('inf')
        # record the depth of the current node being traversed
        self.currentDepth = 0

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # start DFS traversal from the root node
        self.traverse(root)
        return self.minDepthValue

    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return

        # increase the current depth when entering a node in the preorder position
        self.currentDepth += 1

        # if the current node is a leaf, update the minimum depth
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.currentDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        # decrease the current depth when leaving a node in the postorder position
        self.currentDepth -= 1

# Solution 2: Using BFS
class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftMin = self.minDepth(root.left)
        rightMin = self.minDepth(root.right)
        if root.left is None and root.right is None:
            return 1
        if root.left is None and root.right is not None:
            return rightMin + 1
        if root.left is not None and root.right is None:
            return leftMin + 1
        return 1 + min(leftMin, rightMin)
# root 1:
#       1
#     /   \
#    2     3
#  /  \   / \
# 4      5   6

# root 2:
#    1

# root 3: 
#       1
#     /   \
#    2     3
#         / \
#        5   6

if __name__ == "__main__":
    # root1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(6)

    # root2
    root2 = TreeNode(1)

    # root3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.right.left = TreeNode(5)
    root3.right.right = TreeNode(6)
    
    sol = Solution()
    sol2 = Solution2()
    
    print(sol.minDepth(root1))
    print(sol2.minDepth(root1))

    print(sol.minDepth(root2))
    print(sol2.minDepth(root2))

    print("sol minDepth root3:", sol.minDepth(root3))
    print("sol2 minDepth root3:", sol2.minDepth(root3))
    
    print("Max depth:", maxDepth(root3))