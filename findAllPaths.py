from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findallPath(root: TreeNode) -> list:
    result = []
    path = []
    def traverse(root):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            result.append(path[:]) 
        traverse(root.left)
        traverse(root.right)
        path.pop()
    traverse(root)
    return result

if __name__ == "__main__":
    # root 1:
    #       1
    #     /   \
    #    2     3
    #  /  \   / \
    # 4      5   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(6)

    print(findallPath(root1))