class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    # Write your code here
    if root is None:
        return TreeNode(val)
    if root.left is None and val < root.val:
        root.left = TreeNode(val)
        return
    if root.right is None and val > root.val:
        root.right = TreeNode(val)
        return
    if val > root.val:
        insert_into_bst(root.right, val)
    if val < root.val:
        insert_into_bst(root.left, val)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
insert_into_bst(root, 5)

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

print_tree(root)