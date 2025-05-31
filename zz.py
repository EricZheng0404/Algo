class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def levelTraverse(self, root):
        if root is None:
            return self.res
        # root is considered as level 1
        self.traverse(root, 1)
        return self.res
    

    def traverse(self, root, depth):
        if root is None:
            return
        # pre-order position, check if the nodes at level depth have already been stored
        if len(self.res) <= depth + 1:
            # first time entering level depth
            self.res.append([])
        # pre-order position, add the value of root node at level depth
        self.res[depth].append(root.val)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    """
    1
   / \
  2   3
 / \ / \
4  5 6  7
    """
    solution = Solution()
    solution.levelTraverse(root)
    print(solution.res)