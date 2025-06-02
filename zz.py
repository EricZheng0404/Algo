class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root):
    if root is None:
        return 0
    leftCount = count(root.left)
    # print(f"The leftCount is {leftCount}")
    rightcount = count(root.right)
    # print(f"The rightCount is {rightcount}")
    # print(f"node is {root.val}, left is {leftCount}, right is {rightcount}")
    # return 1 + leftCount + rightcount
    sum_ = leftCount + rightcount + 1
    print(f"Node is {root.val}, sum is {sum_}")
    return sum_


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
count(root=root)