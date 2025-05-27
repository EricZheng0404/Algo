class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root):
    if root is None:
        return 0
    leftCount = count(root.left) + 1
    rightCount = count(root.right) + 1
    print(root.val, leftCount, rightCount)
    return leftCount + rightCount

def traverse(root, level):
    if root is None:
        return
    traverse(root.left, level + 1)
    print(root.val, level)
    traverse(root.right, level + 1)
# The tree is like:
#       1
#      / \
#     2   3
#    / \ / 
#   4  5 6  
#  /
# 7

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

traverse(root, 1)
