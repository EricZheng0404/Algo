def target_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return target_sum(root.left, target - root.val) or target_sum(root.right, target - root.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(target_sum(root, 4))