class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    
    sol = Solution()
    print(sol.minDepth(root))