from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node val is {self.val}"

# If we have the target in the tree
def findTargetDFS(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    def traverse(root, target):
        if root is None:
            return False
        if root.val == target:
            return True
        # Return True if target is found in either left or right subtree
        return traverse(root.left, target) or traverse(root.right, target)
    return traverse(root, target)

# Return the node with the target value
def findTargetNodeDFS(root: TreeNode, targetVal: int) -> TreeNode:
    targetNode = None
    
    def traverse(root, targetVal):
        nonlocal targetNode
        if root is None:
            return
        if root.val == targetVal:
            targetNode = root
            return
        traverse(root.left, targetVal)
        traverse(root.right, targetVal)
        
    traverse(root, targetVal)
    return targetNode

def findTargetNodeBST(root: TreeNode, targetVal: int) -> TreeNode:
    targetNode = None 

    def traverse(root, targetVal):
        nonlocal targetNode
        if root is None:
            return # should immediately return in here
        if root.val == targetVal:
            targetNode = root 
        elif root.val > targetVal:
            traverse(root.left, targetVal)
        elif root.val < targetVal:
            traverse(root.right, targetVal)
        
    traverse(root, targetVal)
    return targetNode # Bug fix: Should return targetNode instead of targetVal

def findsmallestNode(root: TreeNode) -> TreeNode:
    targetNode = None 

    def traverse(root):
        nonlocal targetNode
        if root is None:
            return 
        if root.left is None and root.right is None:
            targetNode = root
        traverse(root.left)

    traverse(root)
    return targetNode
            


if __name__ == "__main__":
#     7
#    / \
#   4   9
#  / \   \
# 1   5   10
    root1 = TreeNode(7)
    root1.left = TreeNode(4)
    root1.right = TreeNode(9)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(10)

    

    # result = findTargetNodeDFS(root1, 4)
    # print(result)

    result = findTargetNodeBST(root1, 4)
    print(result)
    print(findsmallestNode(root1))