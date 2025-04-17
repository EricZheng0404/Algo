"""
Given a binary tree, return the sum of all left leaves.

For example, we have leaves 9, 15, 7. Only 9 and 15 are left leaves, 
so we should return 9 + 15 = 24
    3
  /  \
 9   20
 ^   /  \
  15    7
   ^
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    sum = 0
    if root is None:
        return sum
    if root.left:
        if not root.left.left and not root.left.right:
            sum += root.left.val
        else:
            sum += sumOfLeftLeaves(root.left)
    sum += sumOfLeftLeaves(root.right)
    return sum

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sumOfLeftLeaves(root))