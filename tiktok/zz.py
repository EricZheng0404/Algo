def dfs(root):
    if not root:
        return
    print(root.val)
    dfs(root.left)
    dfs(root.right)

def bfs(root):
    if not root:
        return
    queue = [root]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)