class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order: root-left-right
def PreOrderTraversal(root: TreeNode):
    if root is None:
        return
    print(root.val) # pre-order
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)
    
# In-order: left-root-right
def InOrderTraversal(root: TreeNode):
    if root is None:
        return
    InOrderTraversal(root.left)
    print(root.val) # in-order
    InOrderTraversal(root.right)

# Post-order: left-right-root
def PostOrderTraversal(root: TreeNode):
    if root is None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print(root.val) # in-order

# The constructed binary tree looks like this:
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print("Pre-order:")
PreOrderTraversal(root) # output: 1, 2, 4, 3, 5, 6
print("In-order:")
InOrderTraversal(root) # output: 4, 2, 1, 5, 3, 6
print("Post-order:")
PostOrderTraversal(root) # output: 4, 2, 5, 6, 3, 1